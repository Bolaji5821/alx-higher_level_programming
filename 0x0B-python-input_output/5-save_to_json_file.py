#!/usr/bin/python3
"""Module save_to_json_file:
 writes an Object to a text file, using a JSON representation:
"""
import json


def save_to_json_file(obj, filename):
    """writes to a text file"""
    with open(filename, 'w+') as f:
        json.dump(obj, f)
