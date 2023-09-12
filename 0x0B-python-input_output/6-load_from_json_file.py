#!/usr/bin/python3

"""Module defines JSON file-reading function"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a 'JSON file'"""
    with open(filename, 'r') as fl:
        return json.load(fl)
