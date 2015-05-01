import datetime

from .utc_timezone import UTC

FORMAT_NO_FRACTION = '%Y-%m-%dT%H:%M:%SZ'
FORMAT_WITH_FRACTION = '%Y-%m-%dT%H:%M:%S.%fZ'


class utcdatetime(object):
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
