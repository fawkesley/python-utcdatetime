import datetime
import pytz

from nose.tools import assert_equal, assert_raises

from utcdatetime import utcdatetime

UK = pytz.timezone('Europe/London')
SYDNEY = pytz.timezone('Australia/Sydney')


TEST_CASES = [
    (UK.localize(datetime.datetime(2010, 6, 10, 18, 45)),
     utcdatetime(2010, 6, 10, 17, 45)),  # note british summer time -> UTC

    (UK.localize(datetime.datetime(2010, 2, 10, 18, 45)),
     utcdatetime(2010, 2, 10, 18, 45)),  # UK winter time == GMT

    (SYDNEY.localize(datetime.datetime(2015, 12, 2, 7, 30)),
     utcdatetime(2015, 12, 1, 20, 30)),  # note day shift!

    (SYDNEY.localize(datetime.datetime(2015, 6, 6, 18, 30)),
     utcdatetime(2015, 6, 6, 8, 30)),  # Sydney winter time
]


def test_that_from_datetime_rejets_naive_datetimes():
    assert_raises(ValueError, lambda: utcdatetime.from_datetime(
        datetime.datetime(2015, 10, 10, 13, 45)))


def test_from_datetime():
    for dt, expected_utcdatetime in TEST_CASES:
        yield assert_equal, expected_utcdatetime, utcdatetime.from_datetime(dt)
