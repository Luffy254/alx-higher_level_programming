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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON serialization of a list dictionaries

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON serialization of a list of objects to a file

        Args:
            list_objs (list): list of inherited Base instances
        """
        filename = f"{cls.__name__}.json"

        if list_objs is None:
            list_objs = []

        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)

        with open(filename, "w") as jsonfile:
            jsonfile.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns deserialized JSON string

        Args:
            json_string (str): JSON str representation of a list dicts
        """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns class instantiated from dictionary of attributes

        Args:
            **dictionary (dict): key/value pairs of attributes initialized
        """
        if cls.__name__ == "Rectangle":
            new_inst = cls(5, 5)
            new_inst.update(**dictionary)
        if cls.__name__ == "Square":
            new_inst = cls(5)
            new_inst.update(**dictionary)
        return new_inst

    @classmethod
    def load_from_file(cls):
        """Returns list of classes instantiated from file of JSON strings"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        instances = []
        with open(filename, "r") as file:
            obj_dicts = cls.from_json_string(file.read())

        instances = [cls.create(**obj_dict) for obj_dict in obj_dicts]

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write CSV serialization of list of objects to file

        Args:
            list_objs (list): list of inherited Base instances
        """
        file_name = cls.__name__ + '.csv'
        dicts = [cls.to_dictionary(obj) for obj in list_objs]

        field_names = ['id', 'width', 'height', 'x', 'y'] \
            if cls.__name__ == 'Rectangle' else ['id', 'size', 'x', 'y']

        with open(file_name, 'w', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=field_names)
            csv_writer.writeheader()
            csv_writer.writerows(dicts)

    @classmethod
    def load_from_file_csv(cls):
        """Returns list of classes instantiated from CSV file"""
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []

        instances = []
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                obj_data = {key: int(value) for key, value in row.items()}
                instances.append(cls.create(**obj_data))

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using turtle module

        Args:
            list_rectangles (list): list of Rectangle objects
            list_squares (list): list of Square objects
        """
        wn = turtle.Screen()
        wn.bgcolor('light blue')
        wn.title('Turtle')
        ptr = turtle.Turtle()
        ptr.shape('turtle')

        for shape in list_rectangles + list_squares:
            ptr.penup()
            ptr.goto(shape.x, shape.y)
            ptr.pendown()

            if isinstance(shape, Rectangle):
                for i in range(2):
                    ptr.forward(shape.width)
                    ptr.left(90)
                    ptr.forward(shape.height)
                    ptr.left(90)
            elif isinstance(shape, Square):
                for i in range(4):
                    ptr.forward(shape.size)
                    ptr.left(90)
        turtle.done()
