#!/usr/bin/python3

"""Module defines a file-writing function"""


def write_file(filename="", text=""):
    """
    writes a string to a text file

    Args:
        filename:  name of the file to be written
        text: string that will be written to the file
    Returns:
        number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as fl:
        return fl.write(text)
