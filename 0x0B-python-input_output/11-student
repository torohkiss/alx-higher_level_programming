#!/usr/bin/python3
"""A student class"""


class Student:
    """Student class initialized"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=""):
        if type(attrs) is list:
            dict = {}
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
            for attr in attrs:
                if attr in self.__dict__.keys():
                    dict[attr] = self.__dict__[attr]
            return dict
        return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
