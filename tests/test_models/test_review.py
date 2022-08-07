#!/usr/bin/python3
"""
Unittest for Review Class
"""
import contextlib
from models.review import Review
import unittest
from datetime import datetime
from io import StringIO


class TestReviewClass(unittest.TestCase):
    def test_classtype(self):
        """tests class type"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_save_method(self):
        """test save method"""
        review = Review()
        review.name = "prototype"
        review.number = 1
        review.save()
        update_time = review.updated_at
        self.assertEqual(update_time, review.updated_at)
        with self.assertRaises(TypeError):
            review.save(None)


if __name__ == '__main__':
    unittest.main()
