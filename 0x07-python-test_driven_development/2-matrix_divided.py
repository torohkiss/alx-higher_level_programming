#!/usr/bin/python3
"""This function divides elements of a matrix"""

def matrix_divided(matrix, div):
    """Returns a new matrix of divided elements"""
    new_matrix = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    e = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(e)

    if not isinstance(matrix, list) or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(e)

    arr_size = len(matrix[0])
    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError(e)
        if len(row) != arr_size:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for cell in row:
            if (not isinstance(cell, int) and not isinstance(cell, float)):
                raise TypeError(e)
            new_row.append(round(cell / div, 2))
        new_matrix.append(new_row)
     return new_matrix
