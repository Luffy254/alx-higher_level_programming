#!/usr/bin/python3

from sys import stderr


def safe_print_integer_err(value):

    try:
        int_value = int(value)

        print("{:d}".format(int_value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=stderr)
        return False
