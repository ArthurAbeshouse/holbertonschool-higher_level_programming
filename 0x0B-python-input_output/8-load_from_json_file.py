#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """ converts file JSON into obj """
    with open(filename) as f:
        return json.load(f)
