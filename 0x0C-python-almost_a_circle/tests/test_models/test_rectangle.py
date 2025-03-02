from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):
    def setUp(self):
        """Reset the Base.__nb_objects counter before each test"""
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_values(self):

        with self.assertRaises(ValueError):
            Rectangle(-10, 2, 3, -1)
            Rectangle(10, "2")
            r = Rectangle(10, 2)
            r.x = {}
