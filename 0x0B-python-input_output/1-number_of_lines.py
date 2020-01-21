#!/usr/bin/python3


def number_of_lines(filename=""):
    """reads number of lines in file"""
    line_num = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line_num += 1
    return line_num
