#!/usr/bin/python3

"""Module defines MyList class"""


class MyList(list):
    """class tha inherists from a lists

    Public Methods:
        print_sorted() - Prints the list in ascending order
    """

    def print_sorted(self):
        """
        prints the sorted list
        """

        print(sorted(self))
