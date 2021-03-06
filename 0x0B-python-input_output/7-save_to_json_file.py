#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """ writes to a file with json representation """
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(my_obj, f)
