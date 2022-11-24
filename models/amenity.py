#!/usr/bin/python3
"""Module for class Amenity"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents the Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity"""
        super().__init__(*ars, **kwargs)
