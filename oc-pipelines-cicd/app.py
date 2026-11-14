"""Small example application for CI/CD practice."""


def add_numbers(first, second):
    """Return the sum of two numbers."""
    return first + second


def multiply_numbers(first, second):
    """Return the product of two numbers."""
    return first * second


def greet(name):
    """Return a friendly greeting."""
    if not name or not name.strip():
        raise ValueError("name must not be empty")
    return "Hello, {}!".format(name.strip())
