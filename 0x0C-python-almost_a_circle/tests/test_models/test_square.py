from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from contextlib import redirect_stdout
import io
import unittest

class TestSquare(unittest.TestCase):

    def test_square_str(self):
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)

        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
