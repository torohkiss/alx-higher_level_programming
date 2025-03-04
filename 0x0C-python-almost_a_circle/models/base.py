#!/usr/bin/python3
"""The Base model class module"""


import json


class Base:
    """The base model class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return []
        return json.dumps(list_dictionaries)
