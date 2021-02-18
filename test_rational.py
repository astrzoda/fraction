from rational import Rational
import pytest


def test_if_denominator_is_equal_to_zero_then_the_value_error_is_raised():
    with pytest.raises(ValueError):
        Rational(2, 0)


def test_rational_str_looks_like_nominator_slash_denominator():
    rational = Rational(2, 1)
    assert str(rational) == "2/1"


def test_rational_repr_looks_like_initializer_call():
    rational = Rational(10, 2)
    assert repr(rational) == "Rational(10, 2)"


def test_adding_int_to_rational_results_in_rational():
    rational = Rational(2, 3)
    result = rational + 5
    assert repr(result) == repr(Rational(17, 3))


@pytest.mark.parametrize(
    "initial_rational, other_rational, result",
    [
        (Rational(1, 2), Rational(1, 2), Rational(1, 1)),
        (Rational(2, 3), Rational(2, 3), Rational(4, 3)),

    ]
)
def test_adding_rational_to_rational_results_in_rational():
    rational1 = Rational(-1, 2)
    rational2 = Rational(1, 1)
    result = rational1 + rational2
    assert repr(result) == repr(Rational(1, 2))
