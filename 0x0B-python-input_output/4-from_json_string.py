#!/usr/bin/python3

"""Module defines a JSON-to-object function"""
import json


def from_json_string(my_str):
    """function that returns an object represented by a JSON string"""
    return json.loads(my_str)
