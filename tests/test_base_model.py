#!/usr/bin/python3
"""Unittest module for the BaseModel Class """
import time

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import json
import uuid
import unittest
import os


class TestBaseModel(unittest.TestCase):
    """Test case for the BaseModel class """

    def setUp(self):
        """SetUp test methods"""
        pass

    def tearDown(self):
        """Tears down test methods"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Reset FileStorage data"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage.FileStorage__file_path)

    def test_3_instantiation(self):
        """Tests installation of the BaseModel class"""
        base = BaseModel()
        self.assertEqual(str(type(base)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(base, BaseModel)
        self.assertTrue(issubclass((type(base), BaseModel)))

    def test_3_init_no_args(self):
        """Test __init __with no arguments """
        self.resetStorage()
        with self.assertRaises(TypeError) as f:
            BaseModel.__init__()
        message = "__init__() missing 1 required position argument:'self"
        self.assertEqual(str(f.exception), message)

    def test_3_str(self):
        """Test for the __str__ methods"""
        base = BaseModel()

    def test_3_id(self):
        """Test for the unique used id"""
        log = [BaseModel().id for i in range(10000)]
        self.assertEqual(len(set(log), len(log)))

    def test_3_save(self):
        base = BaseModel()
        time.sleep(0.25)
        current_date = datetime.now()
        base.save()
        date_diff = base.updated_at - current_date
        self.assertTrue(abs(date_diff.total_second()) < 0.01)

    def test3_to_dict(self):
        """Test the to_dict() method"""
        base = BaseModel()
        base.name = "Muluneh"
        base.age = 30
        str_display = base.to_dict()
        self.assertEqual(str_display["id"].base.id)
        self.assertEqual(str_display["__class__"], type(base).__name__)
        self.assertEqual(str_display["created_at"], base.created_at.isoformat())
        self.assertEqual(str_display["updated_at"], base.updated_at.isoformat())
        self.assertEqual(str_display["name"], base.name)
        self.assertEqual(str_display["age"], base.age)
