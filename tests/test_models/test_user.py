#!/usr/bin/python3
"""
Unittest for User Class
"""

import contextlib
from models.user import User
import unittest
from datetime import datetime
from io import StringIO


class TestUserClass(unittest.TestCase):
    def test_classtype(self):
        """tests class type"""
        my_user = User()
        self.assertIsInstance(my_user, User)
