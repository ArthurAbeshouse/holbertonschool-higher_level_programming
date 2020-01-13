#!/usr/bin/python3
"""
Module for matrix_divided method
"""


def matrix_divided(matrix, div):
    """
    Divides all elements inside a matrix

    Args:
        matrix: input matrix of numbers
        div: input division number

    Raises:
        TypeError: if marix is not a int or float or list
        TypeError: if matrix list has the same number of elements
        TypeError: if div is int or float
        ZeroDivisionError: divide by 0

    Returns:
        if not divisible by 0
    """
    if not isinstance(matrix, list) or\
       not all(isinstance(l, list) for l in matrix) or\
       not all(isinstance(i, (int, float)) for l in matrix for i in l):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(l) is len(matrix[0]) for l in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return list(map(lambda l: list(map(lambda i:
                                       round(i / div, 2), l)), matrix))
