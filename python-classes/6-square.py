#!/usr/bin/python3
"""
This module defines a Square class.

It includes private attributes 'size' and 'position', with getters
and setters for validation, along with area and print methods.
"""


class Square:
    """
    A class that represents a square.

    Attributes:
        size (int): The length of a side of the square.
        position (tuple): The (x, y) coordinates of the square's position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the Square instance.

        Args:
            size (int): The length of a side of the new square.
            position (tuple): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with type and value validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character # to stdout,
        honoring the position offset.
        """
        if self.__size == 0:
            print("")
            return

        # Print vertical offset (y-coordinate)
        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print("")

        # Print the square rows
        for _ in range(self.__size):
            # Print horizontal offset (x-coordinate) + square row
            print(" " * self.__position[0] + "#" * self.__size)
