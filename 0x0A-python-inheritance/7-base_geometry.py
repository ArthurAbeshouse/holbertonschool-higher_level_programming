#!/usr/bin/python3


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """place holder for area calculation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method for validating the value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
