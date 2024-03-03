#!/usr/bin/python3
"""A square class defined"""
from rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    """def __str__(self):
        return '"[Square]" + "(" + str(self.id) + ")" + str(
        self.x) + "/" + str(self.y) + " " + "-" + " " + str(size)'"""
