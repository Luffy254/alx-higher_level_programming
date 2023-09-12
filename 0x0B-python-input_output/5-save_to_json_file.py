#!/usr/bin/python3

"""Module defines JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using a JSON representation

    Args:
        my_obj: object to be serialized and saved as JSON
        filename: name of the file to which the JSON data will be written
    """
    with open(filename, "w") as fl:
        json.dump(my_obj, fl)
