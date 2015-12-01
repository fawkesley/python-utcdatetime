import datetime

from nose.tools import assert_equal

from utcdatetime.utc_timezone import UTC

summer = datetime.datetime(2015, 6, 21)
winter = datetime.datetime(2015, 1, 21)


def test_repr():
    assert_equal('<UTC>', repr(UTC))


def test_utc_offset_returns_zero_time_delta_in_summer_and_winter():
    assert_equal(datetime.timedelta(0), UTC.utcoffset(summer))
    assert_equal(datetime.timedelta(0), UTC.utcoffset(winter))


def test_tzname_is_UTC_in_summer_and_winter():
    assert_equal('UTC', UTC.tzname(summer))
    assert_equal('UTC', UTC.tzname(winter))


def test_daylight_savings_returns_zero_time_delta_for_summer_and_winter():
    # https://docs.python.org/3/library/datetime.html#datetime.datetime.dst
    assert_equal(datetime.timedelta(0), UTC.dst(summer))
    assert_equal(datetime.timedelta(0), UTC.dst(winter))
