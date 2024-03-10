#!/usr/bin/python3


import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """unittest for triangle"""

    def test_width(self):
        rectangle = Rectangle(5, 3)
        with self.assertRaises(TypeError):
            Rectangle.width("10")
        with self.assertRaises(ValueError):
            rectangle.width = -5
        with self.assertRaises(ValueError):
            rectangle.width = 0

    def test_height(self):
        rectangle = Rectangle(5, 3)
        with self.assertRaises(TypeError):
            Rectangle.height("10")
        with self.assertRaises(ValueError):
            rectangle.height = -5
        with self.assertRaises(ValueError):
            rectangle.height = 0

    def test_x(self):
        rectangle = Rectangle(5, 3)
        with self.assertRaises(TypeError):
            Rectangle.x("10")
        with self.assertRaises(ValueError):
            rectangle.x = -5
        # with self.assertRaises(ValueError):
        #    self.rectangle.x = 0

    def test_y(self):
        rectangle = Rectangle(5, 3)
        with self.assertRaises(TypeError):
            Rectangle.y("10")
        with self.assertRaises(ValueError):
            rectangle.y = -5

    def test_area(self):
        rectangle = Rectangle(5, 3)
        self.assertEqual(rectangle.area(), 15)

    def test_display(self):
        r1 = Rectangle(2, 2)
        ex_output = "##\n##\n"
        outp = StringIO()
        sys.stdout = outp
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(outp.getvalue(), ex_output)

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r1), '[Rectangle] (12) 2/1 - 4/6')
        self.assertEqual(str(r2), '[Rectangle] (4) 1/0 - 5/5')


if __name__ == "__main__":
    unittest.main()
