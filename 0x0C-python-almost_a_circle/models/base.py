#!/usr/bin/python3
import json
import os
import csv
"""Module Base:
    The base class for all other classes of this project
"""


class Base:
    """__nb_objects:
    a private class attribute
    id a public instance attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
