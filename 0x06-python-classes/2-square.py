#!/usr/bin/python3
"""A square class with size"""


class Square:
    """Initializing size as private instance
    attribute
    """

    def __init__(self, size=0):
        """Checking size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
