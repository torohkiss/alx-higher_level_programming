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

        # Create a StringIO object to capture stdout
        captured_output = io.StringIO()

        # Redirect stdout to our StringIO object
        with redirect_stdout(captured_output):
            r1.display()

        # Get the value from the StringIO object
        output1 = captured_output.getvalue()

        # Reset the StringIO object for the next test
        captured_output.truncate(0)
        captured_output.seek(0)

        with redirect_stdout(captured_output):
            r2.display()

        output2 = captured_output.getvalue()

        self.assertEqual(output1, f"####\n####\n####\n####\n####\n####\n")
        self.assertEqual(output2, "##\n##\n")

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1)

        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_display_with_xy(self):
        r1 = Rectangle(2, 3, 2, 2)
        r2 = Rectangle(3, 2, 1, 0)
        r3 = Rectangle(4, 4, 0, 1)

        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            r1.display()
        output1 = captured_output.getvalue()
        expected1 = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(output1, expected1)

        # Reset the StringIO object
        captured_output.truncate(0)
        captured_output.seek(0)

        # Test rectangle with x=1, y=0
        with redirect_stdout(captured_output):
            r2.display()

        output2 = captured_output.getvalue()
        expected2 = " ###\n ###\n"
        self.assertEqual(output2, expected2)

        # Reset and test one more case with x=0, y=1
        captured_output.truncate(0)
        captured_output.seek(0)

        with redirect_stdout(captured_output):
            r3.display()
        output3 = captured_output.getvalue()
        expected3 = "\n####\n####\n####\n####\n"
        self.assertEqual(output3, expected3)
