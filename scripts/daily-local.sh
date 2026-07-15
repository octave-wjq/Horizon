#!/usr/bin/env bash
# Local daily Horizon run (AI digest + Feishu webhook).
# Does NOT git pull / deploy GitHub Pages.
#
# Usage:
#   ./scripts/daily-local.sh
#   HOURS=48 ./scripts/daily-local.sh
#
# macOS launchd example (every day 08:00):
#   cp scripts/com.horizon.daily.plist ~/Library/LaunchAgents/
#   # edit paths inside the plist first
#   launchctl load ~/Library/LaunchAgents/com.horizon.daily.plist
#
# cron example (every day 08:00):
#   0 8 * * * /path/to/Horizon/scripts/daily-local.sh >> /path/to/Horizon/logs/cron.log 2>&1

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
LOG_DIR="${PROJECT_DIR}/logs"
HOURS="${HOURS:-24}"
LOG_PREFIX="[$(date '+%Y-%m-%d %H:%M:%S')]"

mkdir -p "$LOG_DIR"
cd "$PROJECT_DIR"

echo "$LOG_PREFIX Starting Horizon local daily run (hours=${HOURS})..."

# Ensure project venv/deps are present
if command -v uv >/dev/null 2>&1; then
  uv sync --quiet
  uv run horizon --hours "$HOURS"
else
  echo "$LOG_PREFIX ERROR: uv not found in PATH" >&2
  exit 1
fi

echo "$LOG_PREFIX Done."
