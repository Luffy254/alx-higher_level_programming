#!/usr/bin/python3
"""Module that defines Rectangle class and is base subclass"""

from models.base import Base


class Rectangle(Base):
    """ectangle class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes Rectangle instance

        Args:
            width (int): width of the rectangle
            height (int): height of rectangle
            x (int): the x-coordinate
            y (int): the y-coordinate
            id (int): identifier for the instance
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        def validate_integer(value, name):
            """Validates that a value is an integer

            Args:
                value (int): value to be validated
                name (str): name of the variable being validated
            """

            if not isinstance(value, int):
                raise TypeError(f"{name} must be an integer")

        def validate_positive(value, name):
            """Validates that a value is a positive integer

            Args:
                value (int): value to be validated
                name (str): name of the variable being validated
            """
            if value <= 0:
                raise ValueError(f"{name} must be > 0")

        validate_integer(width, "width")
        validate_integer(height, "height")
        validate_integer(x, "x")
        validate_integer(y, "y")

        validate_positive(width, "width")
        validate_positive(height, "height")

        if x < 0:
            raise ValueError("x must be >= 0")

        if y < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        """Fetch width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of the rectangle

        Args:
            value (int): new width of rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """fetch height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of the rectangle

        Args:
            value (int): new height the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Fetch x-coordinate of the rectangle's position"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x-coordinate of the rectangle's position

        Args:
            value (int): new x-coordinate rectangle's position
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """fetch y-coordinate of the rectangle's position"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y-coordinate of the rectangle's position

        Args:
            value (int): new y-coordinate rectangle's position
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate area of rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """print in stdout the rectangle instance"""

        h = self.__height
        w = self.__width
        x = self.__x
        y = self.__y

        for i in range(y):
            print()

        for i in range(h):
            for space in range(x):
                print(" ", end="")
            for y in range(w):
                print("#", end="")
            print()

    def __str__(self):
        """string representation of the instance"""
        class_name = self.__class__.__name__
        w = self.__width
        h = self.__height
        return f"[{class_name}] ({self.id}) {self.__x}/{self.__y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """Update object attributes using positional arguments"""

        if args:
            for attr, val in zip(vars(self), args):
                setattr(self, attr, val)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Convert rectangle object to dictionary."""

        return {
            key.replace('_Rectangle__', ''): value
            for key, value in vars(self).items()
        }
