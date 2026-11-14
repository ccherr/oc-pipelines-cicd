"""Unit tests for app.py."""

import unittest

from app import add_numbers, multiply_numbers, greet


class TestApp(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(4, 3), 12)

    def test_greet(self):
        self.assertEqual(greet("Coursera"), "Hello, Coursera!")

    def test_greet_strips_whitespace(self):
        self.assertEqual(greet("  CI/CD  "), "Hello, CI/CD!")

    def test_greet_rejects_empty_name(self):
        with self.assertRaises(ValueError):
            greet("   ")


if __name__ == "__main__":
    unittest.main()
