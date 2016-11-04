from nose.tools import (
    assert_equal, assert_not_equal, assert_true, assert_false,
    assert_is_instance, assert_raises
)

from datetime import timedelta
from utcdatetime import utcdatetime


UNEQUAL_TEST_CASES = [
    ((2015, 6, 25, 16, 0, 0, 0), (2015, 6, 25, 16, 0, 0, 100)),  # microsec
    ((2015, 6, 25, 16, 0, 0, 0), (2015, 6, 25, 16, 0, 1, 0)),    # sec
    ((2015, 6, 25, 16, 0, 0, 0), (2015, 6, 25, 16, 1, 0, 0)),    # min
    ((2015, 6, 25, 16, 0, 0, 0), (2015, 6, 25, 12, 1, 0, 0)),    # hour
    ((2015, 6, 25, 16, 0, 0, 0), (2015, 6, 30, 16, 0, 0, 0)),    # day
    ((2015, 6, 25, 16, 0, 0, 0), (2015, 5, 25, 16, 0, 0, 0)),    # month
    ((2015, 6, 25, 16, 0, 0, 0), (1998, 5, 25, 16, 0, 0, 0)),    # year
]


def test_can_add_timedelta_to_utcdatetime():
    got = utcdatetime(2016, 10, 7, 16, 0) + timedelta(minutes=15)
    expected = utcdatetime(2016, 10, 7, 16, 15)
    assert_equal(expected, got)


def test_can_subtract_timedelta_from_utcdatetime():
    got = utcdatetime(2016, 10, 7, 16, 0) - timedelta(minutes=15)
    expected = utcdatetime(2016, 10, 7, 15, 45)
    assert_equal(expected, got)


def test_can_add_timedelta_with_plus_equals_operator():
    dt = utcdatetime(2016, 10, 7, 16, 0)
    dt += timedelta(minutes=15)

    expected = utcdatetime(2016, 10, 7, 16, 15)
    assert_equal(expected, dt)


def test_can_add_timedelta_with_minus_equals_operator():
    dt = utcdatetime(2016, 10, 7, 16, 0)
    dt -= timedelta(minutes=15)

    expected = utcdatetime(2016, 10, 7, 15, 45)
    assert_equal(expected, dt)


def test_utcdatetimes_compare_equal_when_equal():
    assert_equal(
        utcdatetime(2016, 10, 7, 15, 0),
        utcdatetime(2016, 10, 7, 15, 0)
    )


def test_utcdatetimes_compare_not_equal_when_not_equal():
    for a, b in UNEQUAL_TEST_CASES:
        yield assert_not_equal, utcdatetime(*a), utcdatetime(*b)


def test_utcdatetime_greater_than_returns_true_when_lhs_after_rhs():
    earlier = utcdatetime(2016, 10, 7, 15, 0)
    later = utcdatetime(2016, 10, 7, 16, 0)

    assert_true(later > earlier)


def test_utcdatetime_greater_than_returns_false_when_lhs_before_rhs():
    earlier = utcdatetime(2016, 10, 7, 15, 0)
    later = utcdatetime(2016, 10, 7, 16, 0)

    assert_false(earlier > later)


def test_utcdatetime_less_than_returns_true_when_lhs_before_rhs():
    earlier = utcdatetime(2016, 10, 7, 15, 0)
    later = utcdatetime(2016, 10, 7, 16, 0)

    assert_true(earlier < later)


def test_utcdatetime_less_than_returns_false_when_lhs_after_rhs():
    earlier = utcdatetime(2016, 10, 7, 15, 0)
    later = utcdatetime(2016, 10, 7, 16, 0)

    assert_false(later < earlier)


def test_later_minus_earlier_returns_positive_timedelta():
    earlier = utcdatetime(2016, 10, 7, 15, 0)
    later = utcdatetime(2016, 10, 7, 16, 0)

    delta = later - earlier
    assert_is_instance(delta, timedelta)
    assert_equal(timedelta(hours=1), delta)


def test_earlier_minutes_later_returns_negative_timedelta():
    earlier = utcdatetime(2016, 10, 7, 15, 0)
    later = utcdatetime(2016, 10, 7, 16, 0)

    delta = earlier - later
    assert_is_instance(delta, timedelta)
    assert_equal(timedelta(hours=-1), delta)


def test_subtracting_inappropriate_type_raises_type_error():
    assert_raises(TypeError, lambda: utcdatetime(2016, 10, 7, 15, 0) - "foo")
