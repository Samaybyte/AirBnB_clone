# !/usr/bin/python3
"""
Unittest for Place Class
"""
import contextlib
from models.place import Place
import unittest
from datetime import datetime
from io import StringIO


class TestPlaceClass(unittest.TestCase):
    def test_classtype(self):
        """tests class type"""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_save_method(self):
        """test save method"""
        place = Place()
        place.name = "prototype"
        place.number = 1
        place.save()
        update_time = place.updated_at
        self.assertEqual(update_time, place.updated_at)
        with self.assertRaises(TypeError):
            place.save(None)


if __name__ == '__main__':
    unittest.main()
