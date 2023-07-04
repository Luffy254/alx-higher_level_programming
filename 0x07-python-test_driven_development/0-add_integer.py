#!/usr/bin/python3


def add_integer(a, b=98):
    """
    adds two integers

    Args:
        a: first integer (int)
        b: second integer (int)

    Returns:
        the sum of a(int) and b(int)

    Raises:
        TypeError: if a or b are not an integer or a float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
