#!/usr/bin/python3
"""from string to obj"""


import json


def from_json_string(my_str):
    """from string to object rep"""
    return json.loads(my_str)
