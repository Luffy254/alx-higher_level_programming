#!/usr/bin/python3

"""Defines function printing names"""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name

    Args:
        first_name (str): first name printed
        last_name (str): last name printed

    Raises:
        TypeError: if first_name or last_name is not a string

    Returns:
        nothing
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = first_name + " " + last_name
    print("My name is", full_name)
