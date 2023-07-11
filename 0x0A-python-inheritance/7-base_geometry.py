#!/usr/bin/python3

"""Module defines a base geometry class BaseGeometrY"""


class BaseGeometry:
    """class for geometry-related operations"""

    def area(self):
        """
        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the given value as an integer

        Args:
            name (str): name of the value
            value: value to be validated

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
