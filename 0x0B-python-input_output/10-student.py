#!/usr/bin/python3

"""Module defines a class Student"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student

         Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student
        If attrs is a list of strings, retrieve only those attributes
        included in the list.
        Args:
            attrs (list): (not a must) the attributes to retrieved.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
