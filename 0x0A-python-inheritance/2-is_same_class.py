#!/usr/bin/python3
"""Module is_same_class:
Returns true if the object is exactly an instance of
the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """isintance method is used to compare the object"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
