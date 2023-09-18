#!/usr/bin/python3
"""Module that defines a Base class."""
import csv
import turtle
import json
import os


class Base:
    """The Base class model"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes base instance

        Args:
            id: int that is identifier for the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
