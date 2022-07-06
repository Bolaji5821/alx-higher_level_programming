#!/usr/bin/python3
"""Module 2-append_write:
    appends a string at the end of the openend file
"""


def append_write(filename="", text=""):
    """appends a string and returns the number of characters added"""

    with open(filename, 'a+') as f:
        return f.write(text)
