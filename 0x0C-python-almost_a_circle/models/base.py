#!/usr/bin/python3
"""A Base class"""

import json


class Base:
    """The base class itself"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """dictionary to JSON String"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json rep to a file"""
        nlist = []
        if list_objs is not None:
            for l in list_objs:
                nlist.append(cls.to_dictionary(l))
        with open("{:s}.json".format(cls.__name__), 'w') as file:
            file.write(cls.to_json_string(nlist))
