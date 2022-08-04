#!/usr/bin/python3
"""Module for file storage class"""
import json
import os.path


class FileStorage:
    """Class for serializes  instances to a JSON file and deserializes JSON file to instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return the dictionary representation of the object"""
        return FileStorage.__objects

    def new(self, obj):
        """ Sets new obj in the __object
         Args:
             -obj:the first argument
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            obj_data = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(obj_data, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v) for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict
