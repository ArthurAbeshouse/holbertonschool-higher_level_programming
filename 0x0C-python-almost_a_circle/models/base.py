#!/usr/bin/python3
""" module for Base class """
from json import dumps, loads
import csv


class Base:
    """ Base class for OOP hierarchy """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns a json representation of the list_dictionary """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves jsonified object to file """
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ unjsonifies a dictonary """
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attribute set """
        if cls.__name__ is "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ load the object from Json file """
        try:
            with open("{}.json".format(cls.__name__), 'r') as f:
                return [cls.create(**obj) for obj in
                        cls.from_json_string(f.read())]
        except Exception:
            return []
