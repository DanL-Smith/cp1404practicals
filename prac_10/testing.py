"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n) if n > 1 else s


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(s):
    """Format a string to begin with a capital letter and end with a perio
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("this is a test")
    'This is a test.'
    """
    return s.capitalize() + "."


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"
    assert test_car.fuel == 0, "Car does not set fuel correctly"
    test_car.add_fuel(100)
    assert test_car.fuel == 100, "Car does not set fuel correctly"


run_tests()
