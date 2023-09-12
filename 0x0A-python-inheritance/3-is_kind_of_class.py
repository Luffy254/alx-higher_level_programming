#!/usr/bin/python3

"""Module defines class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class
    or it's subclasses

    Args:
        obj: object to check
        a_class: class to compare against

    Returns:
        True if obj is an instance or inherited instance of a_class
        otherwise False
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
