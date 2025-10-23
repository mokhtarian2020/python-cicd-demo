def validate_positive_number(number):
    """Validate that a number is positive."""
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    if number <= 0:
        raise ValueError("Number must be positive")
    return True


def format_currency(amount):
    """Format a number as currency."""
    return f"${amount:.2f}"


def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0


def factorial(n):
    """Calculate factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
