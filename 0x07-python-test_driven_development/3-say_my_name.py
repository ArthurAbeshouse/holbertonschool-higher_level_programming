#!/usr/bin/python3
"""
Module for say_my_name method
"""


def say_my_name(first_name, last_name=""):
    """
    prints the first and last name

    Args:
        first_name: first name string
        last_name: last name string, defaults to empty when there's no input

    Raises:
        TypeError: If first_name and last_name are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
