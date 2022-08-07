#!/usr/bin/python3
"""
Unittest for City Class
"""
import contextlib
from models.city import City
import unittest
from datetime import datetime
from io import StringIO


class TestCityClass(unittest.TestCase):
    def test_classtype(self):
        """tests class type"""
        city = City()
        self.assertIsInstance(city, City)

    def test_save_method(self):
        """test save method"""
        city = City()
        city.name = "prototype"
        city.number = 1
        city.save()
        update_time = city.updated_at
        self.assertEqual(update_time, city.updated_at)
        with self.assertRaises(TypeError):
            city.save(None)


if __name__ == '__main__':
    unittest.main()
