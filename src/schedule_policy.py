"""Digest schedule policy: skip weekends and China public holidays."""

from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import Iterable, Optional, Tuple
from zoneinfo import ZoneInfo

SHANGHAI = ZoneInfo("Asia/Shanghai")

# Official 放假 ranges from State Council notices (inclusive).
# These are the days marked as holiday/调休放假 — not 调休上班 days.
# Update yearly when the State Council publishes the next calendar.
_CN_HOLIDAY_RANGES: dict[int, list[tuple[str, str]]] = {
    2025: [
        ("2025-01-01", "2025-01-01"),  # 元旦
        ("2025-01-28", "2025-02-04"),  # 春节
        ("2025-04-04", "2025-04-06"),  # 清明
        ("2025-05-01", "2025-05-05"),  # 劳动节
        ("2025-05-31", "2025-06-02"),  # 端午
        ("2025-10-01", "2025-10-08"),  # 国庆+中秋
    ],
    2026: [
        ("2026-01-01", "2026-01-03"),  # 元旦
        ("2026-02-15", "2026-02-23"),  # 春节
        ("2026-04-04", "2026-04-06"),  # 清明
        ("2026-05-01", "2026-05-05"),  # 劳动节
        ("2026-06-19", "2026-06-21"),  # 端午
        ("2026-09-25", "2026-09-27"),  # 中秋
        ("2026-10-01", "2026-10-07"),  # 国庆
    ],
    2027: [
        ("2027-01-01", "2027-01-03"),  # 元旦（常见安排，若国务院另有通知以通知为准）
        ("2027-02-04", "2027-02-12"),  # 春节
        ("2027-04-03", "2027-04-05"),  # 清明
        ("2027-05-01", "2027-05-05"),  # 劳动节
        ("2027-06-09", "2027-06-11"),  # 端午
        ("2027-09-15", "2027-09-17"),  # 中秋（常见安排）
        ("2027-10-01", "2027-10-07"),  # 国庆
    ],
}


def _parse_ymd(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def _iter_range(start: date, end: date) -> Iterable[date]:
    cur = start
    while cur <= end:
        yield cur
        cur += timedelta(days=1)


def china_holiday_dates(years: Optional[Iterable[int]] = None) -> set[date]:
    """Return the set of China public-holiday off days for the given years."""
    if years is None:
        years = _CN_HOLIDAY_RANGES.keys()
    out: set[date] = set()
    for year in years:
        for start_s, end_s in _CN_HOLIDAY_RANGES.get(year, []):
            out.update(_iter_range(_parse_ymd(start_s), _parse_ymd(end_s)))
    return out


def shanghai_today() -> date:
    return datetime.now(SHANGHAI).date()


def should_skip_digest_day(
    day: Optional[date] = None,
    *,
    skip_weekends: bool = True,
    skip_cn_holidays: bool = True,
) -> Tuple[bool, str]:
    """Return (skip, reason) for Asia/Shanghai calendar day.

    Policy:
    - Skip Saturday/Sunday when ``skip_weekends`` is true.
    - Skip China State-Council holiday/off days when ``skip_cn_holidays`` is true.
    - Weekend rule wins even on 调休上班 Sundays (still no push).
    """
    day = day or shanghai_today()
    if skip_weekends and day.weekday() >= 5:
        names = ("周一", "周二", "周三", "周四", "周五", "周六", "周日")
        return True, f"周末（{names[day.weekday()]} {day.isoformat()}）"
    if skip_cn_holidays and day in china_holiday_dates([day.year, day.year - 1, day.year + 1]):
        return True, f"中国法定节假日（{day.isoformat()}）"
    return False, f"工作日（{day.isoformat()}）"
