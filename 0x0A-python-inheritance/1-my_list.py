#!/usr/bin/python3

"""Module defines MyList class"""


class MyList(list):
    """class that inherists from list

    Public Methods:
        print_sorted() - Prints the list in ascending order
    """

    def __init__(self):
        """method to initialize objects"""
        super().__init__()

    def print_sorted(self):
        """
        prints the sorted list
        """

        print(sorted(self))
