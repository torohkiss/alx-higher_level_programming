#!/usr/bin/python3
"""class to json"""


def class_to_json(obj):
    """from class obj to json str"""
    return obj.__dict__
