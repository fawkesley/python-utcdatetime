import utcdatetime

from nose.tools import assert_equal

import datetime


TEST_CASES = [
    (
        utcdatetime.utcdatetime(2015, 5, 11, 16, 43, 10, 45),
        datetime.time(16, 43, 10, 45)
    ),
]


def test_time_method():
    for utc_dt, expected_time in TEST_CASES:
        yield _assert_time_equals, utc_dt, expected_time


def _assert_time_equals(utc_dt, expected_time):
    got = utc_dt.time()

    assert_equal(expected_time, got)
