#!/usr/bin/python3
class Square:
    """The class that defines a square"""
    def __init__(self, size=0):
        """

        The initialization function for the square class.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif type(size) is 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
