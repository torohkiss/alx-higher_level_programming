#!/usr/bin/python3
"""A class"""


class BaseGeometry:
    """A BaseGeometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(self.value, int):
            raise TypeError(self.value + " must be an integer")
        if self.value <= 0:
            raise ValueError(self.value + " must be greater than 0")
