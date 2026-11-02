"""Runtime dates for model prompts, independent of the model's internal clock."""
from ..models import ContentItem
from ..schedule_policy import SHANGHAI, shanghai_today


def temporal_context(item: ContentItem) -> str:
    published = (
        "unknown (historical recommendation; do not infer publication from collection time)"
        if item.metadata.get("publication_date_unknown") or item.published_at is None
        else item.published_at.astimezone(SHANGHAI).isoformat()
    )
    return (
        f"\nRuntime current date (Asia/Shanghai): {shanghai_today().isoformat()}.\n"
        f"Source-provided publication timestamp: {published}.\n"
        "Use this runtime date, not your training cutoff or an assumed internal date. "
        "Publication, collection and digest dates are distinct. Do not invent a date, "
        "or declare a paper future-dated solely because it is beyond your knowledge cutoff. "
        "Source timestamps are metadata, not proof of independently verified publication. "
        "Correct stale current-date claims in earlier summaries; omit irrelevant date caveats.\n"
    )
