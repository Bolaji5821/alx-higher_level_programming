#!/usr/bin/python3
"""Module 3-to_json_string:
    returns a json formatt of an object(string):
"""
import json


def to_json_string(my_obj):
    """returns a json string"""
    return json.dumps(my_obj)
