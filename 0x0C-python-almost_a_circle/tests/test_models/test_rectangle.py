#!/usr/bin/python3


import unittest
from model.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """unittest for triangle"""
    with self.assertRaises(TypeError):
        width("10")
