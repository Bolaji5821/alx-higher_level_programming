#!/usr/bin/python3
"""Module 0-lookup
This function returns all the attributes and method of an object
"""


def lookup(obj):
    """Returns a list of attributes and methods.

    Parameter: object or class to iterate
    """

    return dir(obj)
