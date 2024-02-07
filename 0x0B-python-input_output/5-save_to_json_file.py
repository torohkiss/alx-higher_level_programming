#!/usr/bin/python3
"""save and dump"""


import json


def save_to_json_file(my_obj, filename):
    """write and save to text file"""
    with open(filename, mode='w') as f:
        return json.dump(my_obj, filename)
