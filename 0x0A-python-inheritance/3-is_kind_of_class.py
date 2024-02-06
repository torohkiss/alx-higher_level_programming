#!/usr/bin/python3
"""Is kind of class function"""


def is_kind_of_class(obj, a_class):
    """checks instance  of class"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
