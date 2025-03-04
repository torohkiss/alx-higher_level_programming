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

    def test_square_values(self):
        s1 = Square(5)

        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

    def test_raises(self):
        s1 = Square(5)

        with self.assertRaises(TypeError):
            s1.size = "9"


    def test_square_size(self):
        s1 = Square(5)

        self.assertEqual(s1.size, 5)

        s1.size = 10

        self.assertEqual(s1.size, 10)

    def test_square_update(self):
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

    def test_to_dictionary_square(self):
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)

        self.assertEqual(str(s1), "[Square] (1) 2/1 - 10")

        s1_dictionary = s1.to_dictionary()
        square_dict_rep = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s1_dictionary, square_dict_rep)
        self.assertEqual(type(s1_dictionary), dict)

        self.assertEqual(str(s2), "[Square] (2) 1/0 - 1")

        s2.update(**s1_dictionary)
        self.assertEqual(str(s2), "[Square] (1) 2/1 - 10")

        self.assertNotEqual(s1, s2)
