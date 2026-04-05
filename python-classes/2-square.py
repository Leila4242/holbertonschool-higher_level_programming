#!/usr/bin/python3
"""
This module defines a Square class.

It includes a private attribute 'size' and validation to ensure
the size is a non-negative integer.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
        __size (int): The length of a side of the square (private).
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance.

        Args:
            size (int): The length of a side of the new square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
