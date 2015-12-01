import datetime
import re

from .utcdatetime import utcdatetime

DATETIME_REGEX = (
    r'(?P<year>\d{4})'
    '-'
    '(?P<month>\d{2})'
    '-'
    '(?P<day>\d{2})'
    'T'
    '(?P<hour>\d{2})'
    ':'
    '(?P<minute>\d{2})'
    ':'
    '(?P<second>\d{2})'
)

FRACTIONAL_SECONDS_REGEX = r'(?P<fractional_second>\.\d+)'

TIMEOFFSET_REGEX = (
    r'(?P<offset_sign>[+-])'
    '(?P<offset_hour>\d{2})'
    ':'
    '(?P<offset_minute>\d{2})'
)

REGEXES = [re.compile(x) for x in [
    (DATETIME_REGEX + 'Z'),
    (DATETIME_REGEX + FRACTIONAL_SECONDS_REGEX + 'Z'),

    (DATETIME_REGEX + TIMEOFFSET_REGEX),
    (DATETIME_REGEX + FRACTIONAL_SECONDS_REGEX + TIMEOFFSET_REGEX),
]]


def parse_datetime_string(string):
    for pattern in REGEXES:
        match = pattern.match(string)
        if match is not None:
            return construct_utcdatetime(match)

    raise ValueError(
        'Failed to parse `{0}` Is it a valid RFC 3339 string? See '
        'https://www.ietf.org/rfc/rfc3339.txt'.format(string))


def construct_utcdatetime(match):
    required_args = [
        int(match.group(x))
        for x in ('year', 'month', 'day', 'hour', 'minute', 'second')]

    try:
        required_args.append(
            convert_fractional_second(float(match.group('fractional_second'))))
    except IndexError:
        pass

    utc_dt = utcdatetime(*required_args)

    try:
        offset_sign = match.group('offset_sign')
        offset_hour = int(match.group('offset_hour'))
        offset_minute = int(match.group('offset_minute'))

    except IndexError:
        pass

    else:
        utc_dt -= make_delta(offset_sign, offset_hour, offset_minute)

    return utc_dt


def convert_fractional_second(fractional_second):
    """
    From a fraction of a second, eg .456, return a number of microseconds.
    """
    return int(round(1000000 * float(fractional_second)))


def make_delta(offset_sign, offset_hour, offset_minute):
    plus_minus = int('{0}1'.format(offset_sign))
    return datetime.timedelta(hours=plus_minus * offset_hour,
                              minutes=plus_minus * offset_minute)
