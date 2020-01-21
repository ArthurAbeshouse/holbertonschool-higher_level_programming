#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    """reads n amount of lines in file"""
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        for line_num in range(nb_lines):
            print(f.readline(), end="")
