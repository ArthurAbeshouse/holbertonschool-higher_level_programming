#!/usr/bin/python3


def class_to_json(obj):
    """ returns dictionary description of json object """
    return dict(vars(obj))
