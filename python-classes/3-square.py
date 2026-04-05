#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    A class that represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance (Obyekt yaradılanda işə düşür).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates the current square area.

        Returns:
            The current square area (size * size).
        """
        return self.__size * self.__size
