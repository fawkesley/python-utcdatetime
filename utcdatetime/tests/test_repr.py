from nose.tools import assert_equal

from utcdatetime import utcdatetime

TEST_CASES = [
    ('utcdatetime(2010, 6, 30, 0, 0)',
     utcdatetime(2010, 6, 30)),

    ('utcdatetime(2010, 6, 30, 18, 0)',
     utcdatetime(2010, 6, 30, 18)),

    ('utcdatetime(2010, 6, 30, 18, 36)',
     utcdatetime(2010, 6, 30, 18, 36)),

    ('utcdatetime(2010, 6, 30, 18, 36, 45)',
     utcdatetime(2010, 6, 30, 18, 36, 45)),

    ('utcdatetime(2010, 6, 30, 18, 36, 45)',
     utcdatetime(2010, 6, 30, 18, 36, 45)),

    ('utcdatetime(2010, 6, 30, 18, 36, 45, 456)',
     utcdatetime(2010, 6, 30, 18, 36, 45, 456)),
]


def test_str_method():
    for expected_repr, utc_datetime in TEST_CASES:
        yield assert_equal, expected_repr, repr(utc_datetime)
