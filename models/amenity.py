#!/usr/bin/python3
"""Module for Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class to represent the Amenity"""
    def __init__(self):
        self.name = ''

