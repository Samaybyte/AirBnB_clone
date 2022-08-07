#!/usr/bin/python3
"""
Unittest for Amenity Class
"""
import contextlib
from models.amenity import Amenity
import unittest
from datetime import datetime
from io import StringIO


class TestAmenityClass(unittest.TestCase):
    def test_classtype(self):
        """tests class type"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_save_method(self):
        """test save method"""
        amenity = Amenity()
        amenity.name = "prototype"
        amenity.number = 1
        amenity.save()
        update_time = amenity.updated_at
        self.assertEqual(update_time, amenity.updated_at)
        with self.assertRaises(TypeError):
            amenity.save(None)


if __name__ == '__main__':
    unittest.main()
