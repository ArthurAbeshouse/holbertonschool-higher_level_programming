#!/usr/bin/python3


def inherits_from(obj, a_class):
    """determines if an object is a true subclass of a class"""
    return isinstance(obj, a_class) and type(obj) != a_class
