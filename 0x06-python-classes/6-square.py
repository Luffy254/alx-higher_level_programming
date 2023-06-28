#!/usr/bin/python3

"""Module difines square class"""


class Square:
    """class representing a square"""

    def __init__(self, size=0):
        """Initializing a square instance

        Args:
            size (int): size of square
            position (tuple): position of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """obtain then return tuple position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position of square

        Args:
            value: poition of square tuple

        Raises:
            TypeError: if position is not tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 \
                or not all(isinstance(num, int) for num in value) \
                or not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns calculated area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """prints square with # character"""
        if self.__size == 0:
            print()
            return

        [print() for i i range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print()
