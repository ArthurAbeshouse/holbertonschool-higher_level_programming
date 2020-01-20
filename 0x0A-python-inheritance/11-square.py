#!/usr/bin/python3
"""Module for Square class"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """subclass representing a rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """method for area of square"""
        return self.__size ** 2

    def __str__(self):
        """Returns a string of the area funciton"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
