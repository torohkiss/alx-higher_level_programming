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
            for each_l in list_objs:
                nlist.append(cls.to_dictionary(each_l))
        with open("{:s}.json".format(cls.__name__), 'w') as file:
            file.write(cls.to_json_string(nlist))

    @staticmethod
    def from_json_string(json_string):
        """from js9n string to dictionary"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """crrate instances"""
        if cls.__name__ == "Square":
            inst = cls(3)
        if cls.__name__ == "Rectangle":
            inst = cls(3, 5)
        inst.update(**dictionary)
        return inst
