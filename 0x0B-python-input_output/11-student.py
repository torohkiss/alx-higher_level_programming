#!/usr/bin/python3
"""A student class"""


class Student:
    """Student class initialized"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            new_dict = {}
            for e in attrs:
                if isinstance(e, str):
                    if hasattr(self, e):
                        new_attr = getattr(self, e)
                        new_dict[e] = new_attr
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
