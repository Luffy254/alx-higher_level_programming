#!/usr/bin/python3

"""Defines function carrying out text indentation"""


def text_indentation(text):
    """
    Prints the given text with 2 new lines after '.', '?', and ':'

    Args:
        text (str): input text

    Raises:
        TypeError: If input is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0

    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
