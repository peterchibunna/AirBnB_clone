#!/usr/bin/python3
"""Module for class Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents the Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity"""
        self.name = ""
        super(Amenity, self).__init__(*args, **kwargs)
