#!/usr/bin/python3
def add_integer(a, b=98):
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
