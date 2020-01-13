#!/usr/bin/python3
"""
Module for text_indentation method
"""


def text_indentation(text):
    """
    parses a string for `.?:`, replaces it with a new line

    Args:
        text: input string

    Raises:
        TypeError: checks if text is a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')
    print("\n".join(list(l.strip() for l in text.split('\n'))), end="")
