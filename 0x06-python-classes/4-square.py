#!/usr/bin/python3

"""Module difines square class"""


class Square:
    """class representing a square"""

    def __init__(self, size=0):
        """Initializing a square instance

        Args:
            size (int): size of square
        """
        self.size = size

    @property
    def size(self):
        """Obtain then return int size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        set size of the square

        Args:
            value: size of square int

        Raises:
            TypeError if not integer
            ValueError if size is less 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns calculated area of the square."""
        return (self.__size ** 2)
