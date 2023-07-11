#!/usr/bin/python3

"""Defines a function that looksup an object's attributes and methods"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object

    Args:
        obj: object to lookup

    """

    return (dir(obj))
