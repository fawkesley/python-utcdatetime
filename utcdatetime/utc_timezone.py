import datetime


class UTCTimezone(datetime.tzinfo):
    """UTC timezone"""

    @staticmethod
    def utcoffset(dt):
        return datetime.timedelta(0)

    @staticmethod
    def tzname(dt):
        return "UTC"

    @staticmethod
    def dst(dt):
        return datetime.timedelta(0)

    @staticmethod
    def __repr__():
        return '<UTC>'

UTC = UTCTimezone()
