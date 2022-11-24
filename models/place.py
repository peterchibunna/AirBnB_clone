#!/usr/bin/python3
"""
This module defines the Place class
which inherits the BaseModel object
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    The Place class which inherits `BaseModel`
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = list()

    def __init__(self, *args, **kwargs):
        """Initializes Place"""
        super().__init__(*args, **kwargs)
