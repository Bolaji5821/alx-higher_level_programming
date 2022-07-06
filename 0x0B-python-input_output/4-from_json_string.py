#!/usr/bin/python3
"""Module from_json_string:
    returns an object (Python data structure) represented by a JSON string:
"""
import json


def from_json_string(my_str):
    """return an object"""
    return json.load(my_str)
