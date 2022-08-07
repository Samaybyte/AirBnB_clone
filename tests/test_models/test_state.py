#!/usr/bin/python3
"""
Unittest for State Class
"""
import contextlib
from models.state import State
import unittest
from datetime import datetime
from io import StringIO


class TestStateClass(unittest.TestCase):
    def test_classtype(self):
        """tests class type"""
        state = State()
        self.assertIsInstance(state, State)


if __name__ == '__main__':
    unittest.main()
