#!/usr/bin/python3

"""Defines function division of a matrix"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix

    Args:
        matrix: a list of lists containing integers or floats
        div: number(int or float) to divide the matrix elements by

    Returns:
        new matrix with all elements divided by the given number
        and rounded to 2 decimal places

    Raises:
        TypeError: if matrix is not a matrix (list of lists) of integers/floats
                   if each row of the matrix is not of the same size
                   if the div is not an int or float
        ZeroDivisionError: if div is equal to 0
    """

    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(isinstance(element, (int, float))
               for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return (new_matrix)
