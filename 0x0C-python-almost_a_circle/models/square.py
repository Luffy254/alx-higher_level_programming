#!/usr/bin/python3
"""Module defines Square class, a subclass of Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes Square instance

        Args:
            size (int): size of the square (both width and height).
            x (int): x-coordinate of square's position.
            y (int): y-coordinate of square's position.
            id (int): identifier for the instance
        """
        super().__init__(size, size, x, y, id)
        
    @property
    def size(self):
        """Fetch size of square"""
        return self.width
        
    @size.setter
    def size(self, value):
        """sets size of square"""
        self.width = value
        self.height = value
        
    def __str__(self):
        """Return a string representation of the object."""
        class_name = type(self).__name__
        x, y = super().x, super().y
        width = super().width
        return f"[{class_name}] ({self.id}) {x}/{y} - {width}"
        
    def update(self, *args, **kwargs):
        """Update instance attributes with arguments."""
        if args:
            attrs = ["width", "height", "x", "y"]
            for i, arg in enumerate(args[:len(attrs)]):
                if attrs[i] == "height":
                    setattr(self, "_Rectangle__height", arg)
                else:
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                if key == "height":
                    setattr(self, "_Rectangle__height", value)
                else:
                    setattr(self, key, value)
                    
    def to_dictionary(self):
        """Convert class attributes to dictionary"""
        dictionary = {}
        for key, value in vars(self).items():
            if key == "_Rectangle__height":
                continue
            elif key == "_Rectangle__width":
                dictionary["size"] = value
            else:
                dictionary[key.replace("_Rectangle__", "")] = value
        return dictionary
