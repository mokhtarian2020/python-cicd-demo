import pytest
from src.main import add_numbers, multiply_numbers, calculate_area


def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(1.5, 2.5) == 4.0


def test_multiply_numbers():
    """Test the multiply_numbers function."""
    assert multiply_numbers(3, 4) == 12
    assert multiply_numbers(-2, 3) == -6
    assert multiply_numbers(0, 5) == 0
    assert multiply_numbers(2.5, 4) == 10.0


def test_calculate_area():
    """Test the calculate_area function."""
    assert calculate_area(5, 3) == 15
    assert calculate_area(10, 10) == 100
    assert calculate_area(2.5, 4) == 10.0


def test_calculate_area_negative_values():
    """Test that calculate_area raises ValueError for negative values."""
    with pytest.raises(ValueError, match="Length and width must be positive"):
        calculate_area(-5, 3)

    with pytest.raises(ValueError, match="Length and width must be positive"):
        calculate_area(5, -3)

    with pytest.raises(ValueError, match="Length and width must be positive"):
        calculate_area(-5, -3)
