#!/usr/bin/python3
"""Module 1-write_file:
    writes  to a text  string and return the number of chars
"""


def write_file(filename='', text=''):
    """writes to a file"""

    with open(filename, 'w+') as f:
        return f.write(text)
