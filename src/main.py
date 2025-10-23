def add_numbers(a, b):
    """Add two numbers together."""
    return a - b  # BUG: This should be + not -


def multiply_numbers(a, b):
    """Multiply two numbers together."""
    return a * b


def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    if length < 0 or width < 0:
        raise ValueError("Length and width must be positive")
    return length * width


def main():
    print("Welcome to the CI/CD Demo Calculator!")
    print(f"5 + 3 = {add_numbers(5, 3)}")
    print(f"4 * 6 = {multiply_numbers(4, 6)}")
    print(f"Rectangle area (5x3) = {calculate_area(5, 3)}")


if __name__ == "__main__":
    main()
