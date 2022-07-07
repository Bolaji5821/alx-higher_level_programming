#!/usr/bin/python3
"""Module 7.add_item:
Adds all argument to a list
and saves it to a json file
"""

import json
import os.path
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = 'add_item.json'

my_list = []

if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
    my_list = load_from_json_file(file_name)

if len(sys.argv) > 1:
    for i in sys.argv[1:]:
        my_list.append(i)

save_to_json_file(my_list, file_name)
