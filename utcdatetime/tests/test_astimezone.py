import pytz

from utcdatetime import utcdatetime

from nose.tools import assert_equal

UK = pytz.timezone('Europe/London')
SYDNEY = pytz.timezone('Australia/Sydney')


TEST_CASES = [
    (utcdatetime(2010, 6, 10, 17, 45),  # note british summer time -> UTC
     UK,
     '2010-06-10T18:45:00+01:00'),

    (utcdatetime(2010, 2, 10, 18, 45),  # UK winter time == GMT, no change
     UK,
     '2010-02-10T18:45:00+00:00'),

    (utcdatetime(2015, 12, 1, 20, 30),  # note day shift!
     SYDNEY,
     '2015-12-02T07:30:00+11:00'),

    (utcdatetime(2015, 6, 6, 8, 30),  # Sydney winter time
     SYDNEY,
     '2015-06-06T18:30:00+10:00'),
]


def test_from_datetime():
    for utc_datetime, timezone, expected_python_datetime in TEST_CASES:
        got_datetime = utc_datetime.astimezone(timezone)
        yield assert_equal, expected_python_datetime, got_datetime.isoformat()
