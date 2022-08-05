#!/usr/bin/python3
"""Module for review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class represent the review """

    def __init__(self):
        self.place_id = ''
        self.user_id = ''
        self.text = ''
