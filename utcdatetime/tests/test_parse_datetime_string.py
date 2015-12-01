import itertools
from nose.tools import assert_equal

import strict_rfc3339


from utcdatetime import utcdatetime
from utcdatetime.parse_datetime_string import make_delta, parse_datetime_string


BASE_DATES = ['2010-01-23T18:30:21']

SECONDS_FRACTIONS = [
    '',      # no fractional part
    '.456',
    '.000456',
]

TIMEZONES = [
    'Z',
    '+00:00',
    '+01:00',
    '-01:00',
]


EXPECTED = {
    '2010-01-23T18:30:21Z': utcdatetime(2010, 1, 23, 18, 30, 21),
    '2010-01-23T18:30:21.456Z': utcdatetime(2010, 1, 23, 18, 30, 21, 456000),
    '2010-01-23T18:30:21.000456Z': utcdatetime(2010, 1, 23, 18, 30, 21, 456),

    '2010-01-23T18:30:21+00:00':
    utcdatetime(2010, 1, 23, 18, 30, 21),

    '2010-01-23T18:30:21.456+00:00':
    utcdatetime(2010, 1, 23, 18, 30, 21, 456000),

    '2010-01-23T18:30:21.000456+00:00':
    utcdatetime(2010, 1, 23, 18, 30, 21, 456),

    '2010-01-23T18:30:21+01:00':
    utcdatetime(2010, 1, 23, 17, 30, 21),

    '2010-01-23T18:30:21.456+01:00':
    utcdatetime(2010, 1, 23, 17, 30, 21, 456000),

    '2010-01-23T18:30:21.000456+01:00':
    utcdatetime(2010, 1, 23, 17, 30, 21, 456),

    '2010-01-23T18:30:21-01:00':
    utcdatetime(2010, 1, 23, 19, 30, 21),

    '2010-01-23T18:30:21.456-01:00':
    utcdatetime(2010, 1, 23, 19, 30, 21, 456000),

    '2010-01-23T18:30:21.000456-01:00':
    utcdatetime(2010, 1, 23, 19, 30, 21, 456),
}


def test_parse_string():
    for base, seconds_fraction, timezone in itertools.product(
            BASE_DATES, SECONDS_FRACTIONS, TIMEZONES):
        datetime_string = '{0}{1}{2}'.format(base, seconds_fraction, timezone)

        assert strict_rfc3339.validate_rfc3339(datetime_string), \
            'Not RFC3339: {}'.format(datetime_string)  # for sanity
        yield _assert_datetime_parse_equals, datetime_string, \
            EXPECTED[datetime_string]


def _assert_datetime_parse_equals(datetime_string, expected_utcdatetime):
    assert_equal(
        expected_utcdatetime,
        utcdatetime.from_string(datetime_string))


def test_make_delta():
    cases = [
        ('+', 1, 0, 3600),
        ('-', 1, 0, -3600),
        ('+', 1, 25, 3600 + (25 * 60)),
        ('-', 1, 25, -3600 - (25 * 60)),
    ]

    for sign, hour, minute, expected in cases:
        yield _assert_make_delta_equals, sign, hour, minute, expected


def _assert_make_delta_equals(sign, hour, minute, expected):
    assert_equal(expected, make_delta(sign, hour, minute).total_seconds())


def test_parse_datetime_string_throws_sensible_error():
    try:
        parse_datetime_string('foo')
    except ValueError as e:
        assert_equal(
            'Failed to parse `foo` Is it a valid RFC 3339 string? '
            'See https://www.ietf.org/rfc/rfc3339.txt',
            str(e))
    else:
        assert False, "Didn't raise ValueError"
