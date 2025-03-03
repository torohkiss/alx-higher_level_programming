from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from contextlib import redirect_stdout
import io
import unittest

class TestSquare(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_str(self):
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)

        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")

    def test_square_area(self):
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)

        self.assertEqual(s1.area(), 25)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 9)

    def test_square_display(self):
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)

        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            s1.display()
        output1 = captured_output.getvalue()
        expected1 = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(output1, expected1)

        captured_output.truncate(0)
        captured_output.seek(0)

        with redirect_stdout(captured_output):
            s2.display()
        output2 = captured_output.getvalue()
        expected2 = "  ##\n  ##\n"
        self.assertEqual(output2, expected2)
