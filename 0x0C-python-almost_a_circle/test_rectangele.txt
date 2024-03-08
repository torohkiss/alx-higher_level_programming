#!/usr/bin/python3
"""the rectangle unittest class"""


import os
import pep8
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models import rectangle
Rectangle = rectangle.Rectangle


class TestPep8(unittest.TestCase):
        """Pep8 models/rectangle.py"""
        def test_pep8(self):
            """Pep8"""
            style = pep8.StyleGuide(quiet=False)
            errors = 0
            files = ["models/rectangle.py", "tests/test_models/test_rectangle.py"]
            errors += style.check_files(files).total_errors
            self.assertEqual(errors, 0, 'Need to fix Pep8')


class TestRectangle(unittest.TestCase):
    """rectangle test class"""
    def test_width(self):
        with self.assertRaises(TypeError):
            width('a')


if __name__== "__main__":
    unittest.main()
