#!/usr/bin/python3

"""Module defines a file-appending function"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file

    Args:
        filename:  name of the file to which the string will be appended
        text: string to be appended
    Returns:
        number of characters added
    """
    with open(filename, "a", encoding="utf-8") as fl:
        return fl.write(text)
