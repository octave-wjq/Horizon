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


def test_download_window_includes_previous_five_calendar_days():
    from src.schedule_policy import download_catchup_dates
    assert download_catchup_dates(date(2026, 10, 30)) == [date(2026, 10, d) for d in range(25, 31)]
    assert download_catchup_dates(date(2026, 10, 31)) == []
    assert download_catchup_dates(date(2026, 10, 1)) == []
    assert download_catchup_dates(date(2026, 11, 2))[0] == date(2026, 10, 28)
