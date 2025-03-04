from models.rectangle import Rectangle
from models.base import Base
import json
import unittest


class TestModels(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}

        self.assertEqual(dictionary, expected_dict)
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(json.loads(json_dictionary), [dictionary])
        self.assertIsInstance(json_dictionary, str)


