#!/usr/bin/python3
"""Module for class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents class Review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes Review"""
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super(Review, self).__init__(*args, **kwargs)
