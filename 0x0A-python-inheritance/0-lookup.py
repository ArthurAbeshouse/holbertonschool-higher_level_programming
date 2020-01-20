#!/usr/bin/python3


def lookup(obj):
    """Looks up object attributes and methods
    Args:
        obj (object): the object to list
    Returns:
        list: the list of attributes and methods

"""
return dir(obj)
