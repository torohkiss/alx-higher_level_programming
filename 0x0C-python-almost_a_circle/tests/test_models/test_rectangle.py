from models.rectangle import Rectangle
from models.base import Base
import io
from contextlib import redirect_stdout
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

    def test_area(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)

        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        r1 = Rectangle(4, 6)
        r2 = Rectangle(2, 2)

        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            r1.display()

        output = captured_output.getvalue()

        self.assertEqual(output, f"####\n####\n####\n####\n####\n####\n")
