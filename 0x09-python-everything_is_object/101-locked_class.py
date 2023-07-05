#!/usr/bin/python3

"""Defines a class that is locked"""


class LockedClass:
    """
    limits user from dynamically creating new instance attributes
    if not called first_name
    """

    __slots__ = ["first_name"]
