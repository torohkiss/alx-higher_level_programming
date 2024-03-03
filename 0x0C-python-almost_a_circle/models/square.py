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

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
