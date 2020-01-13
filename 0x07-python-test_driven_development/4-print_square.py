#!/usr/bin/python3
"""
Module for print_square method
"""


def print_square(size):
    """
    prints a square made out of # characters

    Args:
        size: the size of the square's side

    Raises:
        TypeError: If size is not an int
        ValueError: If size is < 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print('#' * size)
