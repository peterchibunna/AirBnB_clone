#!/usr/bin/python3
"""
This module defines the City class
which inherits the BaseModel object
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    The City class which inherits `BaseModel`
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes City"""
        self.state_id = ""
        self.name = ""
        super(City, self).__init__(*args, **kwargs)
