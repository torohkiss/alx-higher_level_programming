#!/usr/bin/python3
"""A square module that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class that inherits from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading __str__ method for a different return"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
