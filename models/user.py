#!/usr/bin/python3
"""Module for user """
from models.base_model import BaseModel


class User:
    """class for user"""
    def __init__(self):
        """Initialize the public class attribute"""
        self.email = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
