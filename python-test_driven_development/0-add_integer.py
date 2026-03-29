#!/usr/bin/python3
"""
This module provides a function `add_integer` that adds two numbers.
It handles integers and floats, casting floats to integers before addition.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float (defaults to 98).

    Raises:
        TypeError: If a or b are not integers or floats.

    Returns:
        The sum of a and b as an integer.
    """
    sum = 0
    try:
        if isinstance(a, float) or isinstance(b, float):
            sum = int(a) + int(b)
        else:
            sum = a + b
    except TypeError:
        if not isinstance(a, int):
            raise TypeError("a must be an integer")
        if not isinstance(b, int):
            raise TypeError("b must be an integer")
    return sum
