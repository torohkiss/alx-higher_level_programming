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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size * self.__size)
