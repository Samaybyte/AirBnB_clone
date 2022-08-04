#!/usr/bin/python3
"""Module for Base class """
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """Class for the base model of object hierarchy"""

    def __init__(self, *args, **kwargs):
        """Initialize of the base instance
        Args:
            -*args: list of argument
            -**kwargs:dict of key-values argument
        """
        if kwargs:
            del kwargs['__class__']
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.created_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return the string representation of an instance"""
        return "[{}] ({}) ({})".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the update_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return the dictionary representation of an instance"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
