#!/usr/bin/python3
"""
This module defines the State class
which inherits the BaseModel object
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    The State class which inherits `BaseModel`
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes State"""
        self.name = ""
        super(State, self).__init__(*args, **kwargs)
