"""Unittest for base class"""
import unittest
import pep8
import json
import os
from models import base
from models import rectangle
Base = base.Base
Rectangle = rectangle.Rectangle



class TestBaseClass(unittest.TestCase):
    """the test init"""

    def test_to_json_string(self):

