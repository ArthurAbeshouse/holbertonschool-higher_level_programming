#!/usr/bin/python3


def inherits_from(obj, a_class):
    """returns if obj is either a_class or inherited from a_class"""
    return isinstance(obj, a_class) and type(obj) != a_class
