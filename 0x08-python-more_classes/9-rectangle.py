#!/usr/bin/python3

"""Module defines a Rectangle class"""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize a new rectangle instance
        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieve width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area of the rectangle

        Returns:
            Area of the rectangle int
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter of the rectangle

        Returns:
            Perimeter of the rectangle int
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """Return a string representation of the rectangle
        using print_symbol characters
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rect = ""
            for i in range(self.__height):
                rect += str(self.print_symbol) * self.__width + "\n"
        return rect[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """Print a message whenever an instance of Rectangle gets deleted"""

        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to compare rectangles based on area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method to create square rectangle"""
        return cls(size, size)
