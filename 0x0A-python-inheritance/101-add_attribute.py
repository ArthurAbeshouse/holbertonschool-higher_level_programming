#!/usr/bin/python3


def add_attribute(a_class, new_attr, value):
    """
    if the object has a __dict__, add the new attribute
    if not, raise TypeError
    """
    if not hasattr(a_class, '__dict__'):
        raise TypeError('can\'t add new attribute')
    setattr(a_class, new_attr, value)
