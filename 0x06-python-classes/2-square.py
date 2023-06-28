#!/usr/bin/python3

"""Module difines square class"""


class Square:
    """class representing a square"""

    def __init__(self, size=0):
        """Initializing a square instance

        Args:
            size (int): size of square

        Raises:
            ValueError: if size is less than 0
            TypeError: if size is not an integer
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
