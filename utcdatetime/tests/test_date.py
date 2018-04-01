import utcdatetime

from nose.tools import assert_equal

import datetime


TEST_CASES = [
    (
        utcdatetime.utcdatetime(2015, 5, 11, 16, 43, 10, 45),
        datetime.date(2015, 5, 11)
    ),
]


def test_date_method():
    for utc_dt, expected_date in TEST_CASES:
        yield _assert_date_equals, utc_dt, expected_date


def _assert_date_equals(utc_dt, expected_date):
    got = utc_dt.date()

    assert_equal(expected_date, got)
