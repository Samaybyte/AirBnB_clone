#!/usr/bin/python3

from datetime import datetime
import uuid


class BaseModel:

    def __init__(self, *args, **kwargs):
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
        return "[{}] ({}) ({})".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
