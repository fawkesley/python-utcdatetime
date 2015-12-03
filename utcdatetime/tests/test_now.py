import utcdatetime

from nose.tools import assert_equal
from freezegun import freeze_time

from datetime import datetime


TEST_CASES = [
    (datetime(2015, 5, 11, 16, 43), (2015, 5, 11, 16, 43, 0)),
]


def test_now_method():
    for local_datetime, expected_utc in TEST_CASES:
        yield _assert_now_equals, local_datetime, expected_utc


def _assert_now_equals(local_datetime, expected_utc):
    with freeze_time(local_datetime):
        got = utcdatetime.utcdatetime.now()

    assert_equal(utcdatetime.utcdatetime(*expected_utc), got)
