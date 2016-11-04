import datetime
from functools import total_ordering

from .utc_timezone import UTC

FORMAT_NO_FRACTION = '%Y-%m-%dT%H:%M:%SZ'
FORMAT_WITH_FRACTION = '%Y-%m-%dT%H:%M:%S.%fZ'


@total_ordering
class utcdatetime(object):
    @classmethod
    def from_string(cls, string):
        from .parse_datetime_string import parse_datetime_string
        return parse_datetime_string(string)

    @classmethod
    def from_datetime(cls, dt):
        dt_utc = dt.astimezone(UTC)

        return cls(dt_utc.year, dt_utc.month, dt_utc.day, dt_utc.hour,
                   dt_utc.minute, dt_utc.second, dt_utc.microsecond)

    @classmethod
    def now(cls):
        """
        Return the current date and time in the UTC timezone.
        """
        return cls.from_datetime(datetime.datetime.now(UTC))

    def astimezone(self, tz):
        """
        https://docs.python.org/2/library/datetime.html#datetime.datetime.astimezone
        Return a Python datetime object with tzinfo attribute tz.
        """
        return self.__dt.astimezone(tz)

    def __init__(self, year, month, day, hour=0, minute=0, second=0,
                 microsecond=0):
        self.__dt = datetime.datetime(year, month, day, hour, minute, second,
                                      microsecond, tzinfo=UTC)

    def __str__(self):
        return self.__dt.strftime(
            FORMAT_WITH_FRACTION if self.__dt.microsecond > 0
            else FORMAT_NO_FRACTION)

    def __repr__(self):
        parts = [self.__dt.year, self.__dt.month, self.__dt.day,
                 self.__dt.hour, self.__dt.minute]

        if self.__dt.second > 0:
            parts.append(self.__dt.second)

        if self.__dt.microsecond > 0:
            parts.append(self.__dt.microsecond)

        return 'utcdatetime({0})'.format(', '.join(
            ['{0}'.format(part) for part in parts]))

    def __eq__(self, other):
        return self.__dt == other.__dt

    def __lt__(self, other):
        return self.__dt < other.__dt

    def __add__(self, delta):
        return self.from_datetime(self.__dt + delta)

    def __sub__(self, other):
        if isinstance(other, datetime.timedelta):
            return self.from_datetime(self.__dt - other)

        if isinstance(other, utcdatetime):
            return self.__dt - other.__dt

        raise TypeError("Can't do utcdatetime - type {}".format(
            type(other)))
