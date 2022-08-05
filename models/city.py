#!/usr/bin/pytnon3
"""Module for City"""
from models.base_model import BaseModel


class City(BaseModel):
    """class for representing the city"""
    def __init__(self):
        self.sate_id = ''
        self.name = ''

