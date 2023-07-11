#!/usr/bin/python3

"""Module defines class-checking function"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class

    Args:
        obj:  object to check
        a_class: class to compare against

    Returns:
        True if the object is exactly an instance of the class
        or False otherwise
    """

    if type(obj) == a_class:
        return True
    else:
        return False
