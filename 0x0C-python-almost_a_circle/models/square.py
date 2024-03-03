#!/usr/bin/python3
"""A square class defined"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class that inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """The __init__ method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """the size props"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """string representation"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
