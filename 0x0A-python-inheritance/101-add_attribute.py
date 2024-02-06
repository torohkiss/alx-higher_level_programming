#!/usr/bin/python3
"""adds a new attribute to an object"""


def add_attribute(cls, name, value):
    """adds a new attribute to an object"""
    if hasattr(cls, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(cls, name, value)
