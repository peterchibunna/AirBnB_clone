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
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super(User, self).__init__(*args, **kwargs)
