"""Storage manager for configuration and state persistence."""

import json
import os
import re
import shutil
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from .._file_utils import _atomic_write_text
from ..models import Config


# Matches ${VAR_NAME} in string config values. Names follow env-var rules
# (ASCII letters, digits, underscore; must not start with a digit).
_ENV_VAR_PATTERN = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}")


def safe_output_path(root: Path, filename: str) -> Path:
    """Return an output path only when it resolves below root."""
    resolved_root = root.resolve()
    candidate = (resolved_root / filename).resolve()
    if candidate.parent != resolved_root:
        raise ValueError(f"Output path escapes intended root: {candidate}")
    return candidate


def _expand_env_vars(value: Any) -> Any:
    """Recursively expand ``${VAR}`` references inside any string leaves.

    Containers (dicts, lists, tuples) are walked; non-string leaves are
    returned unchanged. Strings with no ``${...}`` tokens are returned
    unchanged. References to unset variables are **left as-is**, so
    ``${MISSING}`` round-trips to ``${MISSING}`` and surfaces as a clear
    downstream error rather than a silent empty string.

    This is intentionally identical to the behaviour ``RSSScraper`` uses
    for RSS feed URLs, so a single ``${VAR}`` convention works everywhere
    in the config (AI ``base_url``, feed URLs, webhook URLs, ...).
    """
    if isinstance(value, str):
        return _ENV_VAR_PATTERN.sub(
            lambda m: os.environ.get(m.group(1), m.group(0)),
            value,
        )
    if isinstance(value, dict):
        return {k: _expand_env_vars(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_expand_env_vars(v) for v in value]
    if isinstance(value, tuple):
        return tuple(_expand_env_vars(v) for v in value)
    return value


class ConfigError(ValueError):
    """Raised when configuration is missing or invalid."""

    pass


class StorageManager:
    """Manages file-based storage for configuration and state."""

    # Durable cross-day dedup ledger (tracked in git so CI has history).
    SEEN_ITEMS_FILENAME = "seen_items.json"
    SEEN_ITEMS_MAX = 500

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.config_path = self.data_dir / "config.json"
        self.summaries_dir = self.data_dir / "summaries"
        self.seen_items_path = self.data_dir / self.SEEN_ITEMS_FILENAME

        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.summaries_dir.mkdir(parents=True, exist_ok=True)

    def load_config(self) -> Config:
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}\n"
                f"Please create it based on the template in README.md"
            )

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise ConfigError(
                f"Invalid JSON in configuration file: {self.config_path}\n" f"Error: {e}"
            ) from e

        # Expand ${VAR} references in every string value before pydantic
        # validation. Keeps credentials / private endpoints / tenant IDs
        # out of the JSON file so it is safe to commit to a public repo.
        data = _expand_env_vars(data)

        try:
            return Config.model_validate(data)
        except ValidationError as e:
            raise ConfigError(
                f"Configuration validation failed for {self.config_path}\n"
                f"Details: {e}"
            ) from e

    def save_config(self, config: Config, backup: bool = True) -> Path:
        """Save configuration to config.json, optionally backing up the existing file.

        Args:
            config: The Config object to save.
            backup: If True and config.json exists, copy it to config.json.bak first.

        Returns:
            Path to the saved config file.
        """
        if backup and self.config_path.exists():
            shutil.copy2(self.config_path, self.config_path.with_suffix(".json.bak"))

        content = json.dumps(
            config.model_dump(mode="json"), indent=2, ensure_ascii=False
        )
        _atomic_write_text(self.config_path, f"{content}\n")

        return self.config_path

    def save_daily_summary(self, date: str, markdown: str, language: str = "en") -> Path:
        filename = f"horizon-{date}-{language}.md"
        filepath = safe_output_path(self.summaries_dir, filename)

        _atomic_write_text(filepath, markdown)

        return filepath

    def load_seen_items(self) -> list[dict]:
        """Load durable seen-item records used for cross-day digest dedup."""
        if not self.seen_items_path.exists():
            return []
        try:
            with open(self.seen_items_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            return []
        if isinstance(data, dict):
            items = data.get("items", [])
        elif isinstance(data, list):
            items = data
        else:
            items = []
        return [item for item in items if isinstance(item, dict)]

    def save_seen_items(self, items: list[dict]) -> Path:
        """Persist seen-item records (newest last; keep only SEEN_ITEMS_MAX)."""
        trimmed = items[-self.SEEN_ITEMS_MAX :]
        payload = {
            "version": 1,
            "updated_at": __import__("datetime").datetime.now(
                __import__("datetime").timezone.utc
            ).isoformat(),
            "items": trimmed,
        }
        _atomic_write_text(
            self.seen_items_path,
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        )
        return self.seen_items_path

    def record_seen_digest_items(
        self,
        items: list,
        *,
        date: str,
        url_key_fn,
        title_key_fn,
        extra_keys_fn=None,
    ) -> Path:
        """Append selected digest items into the durable seen ledger."""
        existing = self.load_seen_items()
        known = {
            (rec.get("url_key"), rec.get("title_key"))
            for rec in existing
            if rec.get("url_key") or rec.get("title_key")
        }
        for item in items:
            title = getattr(item, "title", "") or ""
            url = str(getattr(item, "url", "") or "")
            url_key = url_key_fn(url) if url else ""
            title_key = title_key_fn(title) if title else ""
            pair = (url_key, title_key)
            if pair in known:
                continue
            rec = {
                "date": date,
                "title": title,
                "url": url,
                "url_key": url_key,
                "title_key": title_key,
                "id": getattr(item, "id", None),
            }
            if extra_keys_fn is not None:
                extras = extra_keys_fn(item) or []
                rec["extra_keys"] = list(extras)
            existing.append(rec)
            known.add(pair)
        return self.save_seen_items(existing)

    def load_subscribers(self) -> list:
        """Loads the list of email subscribers."""
        subscribers_path = self.data_dir / "subscribers.json"
        if not subscribers_path.exists():
            return []

        try:
            with open(subscribers_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def add_subscriber(self, email_addr: str):
        """Adds a new subscriber email."""
        subscribers = self.load_subscribers()
        if email_addr not in subscribers:
            subscribers.append(email_addr)
            self._save_subscribers(subscribers)

    def remove_subscriber(self, email_addr: str):
        """Removes a subscriber email."""
        subscribers = self.load_subscribers()
        if email_addr in subscribers:
            subscribers.remove(email_addr)
            self._save_subscribers(subscribers)

    def _save_subscribers(self, subscribers: list):
        """Helper to save subscribers list."""
        subscribers_path = self.data_dir / "subscribers.json"
        _atomic_write_text(subscribers_path, json.dumps(subscribers, indent=2))
