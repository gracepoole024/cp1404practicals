"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


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


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    car = Car(fuel=10)
    assert car.fuel == 10

    car = Car()
    assert car.fuel == 0


def format_as_sentence(phrase):
    """
        Format a phrase as a proper sentence:
        - Capitalize the first letter
        - Ensure it ends with exactly one full stop
        - Do not add a full stop if one already exists

        >>> format_as_sentence("hello")
        'Hello.'
        >>> format_as_sentence("It is an ex parrot.")
        'It is an ex parrot.'
        >>> format_as_sentence("what a lovely day")
        'What a lovely day.'
        >>> format_as_sentence("hi.")
        'Hi.'
        >>> format_as_sentence("")
        '.'
        """
    phrase = phrase.strip()

    sentence = phrase[0].upper() + phrase[1:]

    if sentence[-1] != '.':
        sentence = f"{sentence}."
    return sentence


run_tests()

doctest.testmod()
