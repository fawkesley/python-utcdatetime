from nose.tools import assert_equal

from utcdatetime import utcdatetime

TEST_CASES = [
    ('2010-06-30T00:00:00Z', utcdatetime(2010, 6, 30)),
    ('2010-06-30T18:00:00Z', utcdatetime(2010, 6, 30, 18)),
    ('2010-06-30T18:36:00Z', utcdatetime(2010, 6, 30, 18, 36)),
    ('2010-06-30T18:36:45Z', utcdatetime(2010, 6, 30, 18, 36, 45)),
    ('2010-06-30T18:36:45Z', utcdatetime(2010, 6, 30, 18, 36, 45)),
    ('2010-06-30T18:36:45.000456Z', utcdatetime(2010, 6, 30, 18, 36, 45, 456)),
]


def test_str_method():
    for expected_string, utc_datetime in TEST_CASES:
        yield assert_equal, expected_string, str(utc_datetime)
