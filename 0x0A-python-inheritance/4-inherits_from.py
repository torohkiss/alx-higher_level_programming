#!/usr/bin/python3
"""Subclass function"""


def inherits_from(obj, a_class):
    """returns subclass"""

    if issubclass(obj, a_class):
        return True
    else:
        return False
