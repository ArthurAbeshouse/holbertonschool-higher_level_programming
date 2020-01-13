#!/usr/bin/python3
"""
Module for add_integer method
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a: the first integer
        b: the second integer, defaults to 98 if no input

    Raises:
        TypeError: if a or b is not a int or float

    Returns:
        The sum of two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
