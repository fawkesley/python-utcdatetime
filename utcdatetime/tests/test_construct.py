from nose.tools import assert_raises


from utcdatetime import utcdatetime


def test_good_constructors():
    valid_args = [
        (2015, 6, 30),
        (2015, 6, 30, 18),
        (2015, 6, 30, 18, 45),
        (2015, 6, 30, 18, 45, 37),
        (2015, 6, 30, 18, 45, 37, 500),
    ]

    for args in valid_args:
        yield _assert_can_construct, args


def _assert_can_construct(args):
    utcdatetime(*args)


def test_bad_constructors():
    valid_args = [
        [],
        (2015),
        (2015, 6),
        (2015, 6, 30),
        (2015, 6, 30, 18, 45, 37, 500, None),
    ]

    for args in valid_args:
        yield assert_raises, TypeError, lambda: utcdatetime(args)


def test_valid_month_are_accepted():
    for month in range(1, 12 + 1):
        yield _assert_can_construct, (2015, month, 1)


def test_invalid_months_are_rejected():
    for month in [0] + list(range(13, 32)):
        yield assert_raises, TypeError, (2015, month, 1)


def test_invalid_days_are_rejected():
    invalid_dates = [
        (2000, 1, 0),

        (2000, 1, 32),
        (2000, 2, 30),  # leap year
        (2001, 2, 29),  # non leap year
        (2000, 3, 32),
        (2000, 4, 31),
        (2000, 5, 32),
        (2000, 6, 31),
        (2000, 7, 32),
        (2000, 8, 32),
        (2000, 9, 31),
        (2000, 10, 32),
        (2000, 11, 31),
        (2000, 12, 32),
    ]

    for args in invalid_dates:
        yield assert_raises, ValueError, lambda: utcdatetime(*args)
