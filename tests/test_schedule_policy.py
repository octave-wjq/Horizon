from datetime import date

from src.schedule_policy import should_skip_digest_day


def test_skip_weekend():
    skip, reason = should_skip_digest_day(date(2026, 8, 15))  # Saturday
    assert skip
    assert "周末" in reason


def test_skip_cn_holiday_spring_festival():
    skip, reason = should_skip_digest_day(date(2026, 2, 18))  # during 春节
    assert skip
    assert "法定节假日" in reason


def test_workday_runs():
    skip, reason = should_skip_digest_day(date(2026, 8, 19))  # Wednesday
    assert not skip
    assert "工作日" in reason
