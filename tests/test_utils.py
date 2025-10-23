import pytest
from src.utils.math_helpers import (
    validate_positive_number,
    format_currency,
    is_even,
    factorial,
)


def test_validate_positive_number():
    """Test the validate_positive_number function."""
    assert validate_positive_number(5) is True
    assert validate_positive_number(3.14) is True

    with pytest.raises(ValueError, match="Number must be positive"):
        validate_positive_number(-1)

    with pytest.raises(ValueError, match="Number must be positive"):
        validate_positive_number(0)

    with pytest.raises(TypeError, match="Input must be a number"):
        validate_positive_number("5")


def test_format_currency():
    """Test the format_currency function."""
    assert format_currency(10) == "$10.00"
    assert format_currency(3.14159) == "$3.14"
    assert format_currency(0) == "$0.00"


def test_is_even():
    """Test the is_even function."""
    assert is_even(2) is True
    assert is_even(4) is True
    assert is_even(1) is False
    assert is_even(3) is False
    assert is_even(0) is True


def test_factorial():
    """Test the factorial function."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(3) == 6

    with pytest.raises(
        ValueError, match="Factorial is not defined for negative numbers"
    ):
        factorial(-1)
