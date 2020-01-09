#!/usr/bin/python3


class Square:
    """The class that defines a square"""

    def __init__(self, size=0):
        """
        The initialization function for the square class.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """size properties"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the size of the square"""
        return self.__size ** 2

    def my_print(self):
        """print the square"""
        for y in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()
