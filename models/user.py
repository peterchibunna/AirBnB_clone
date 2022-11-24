#!/usr/bin/python3
"""
This module defines the User class
which inherits the BaseModel object
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class which inherits `BaseModel`
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initializes User"""
        super().__init__(*args, **kwargs)
