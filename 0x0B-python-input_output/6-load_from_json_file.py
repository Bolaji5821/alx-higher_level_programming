#!/usr/bin/python3
"""Module 6-load_from_json_file:
 creates an Object from a JSON file
"""
import json


def load_from_json_file(filename):
    """creates an object"""
    with open(filename, 'r') as f:
        return json.load(f)
