#!/usr/bin/python3

"""Module defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from a specified class

    Args:
        obj: object to check
        a_class: class to compare against

    Returns:
        True if obj is an inherited instance of a_class
        otherwise False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
