#!/usr/bin/python3
"""
This is the base models for all the tasks in this module
"""
import csv
import json
import os
import uuid
import datetime
from models import storage


class BaseModel:
    """
    The Base model
    """

    def __init__(self, *args, **kwargs):
        """
        We are initializing the BaseModel object with id
        :param *args: Argument list
        :param *kwargs: Keyword Argument dictionary
        """
        # storage.reload()
        # fixme: this line above causes recursion during creation of
        #  model instance from json
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = uuid.uuid4().__str__()
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(o=self)

    def __str__(self):
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Upon save, we should update the `updated_at`
        property with the current time
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        Converts the instance to a dictionary
        :return: the model instance as `json`
        """
        _dict = self.__dict__.copy()
        _dict['__class__'] = self.__class__.__name__
        _dict['created_at'] = _dict['created_at'].isoformat()
        _dict['updated_at'] = _dict['updated_at'].isoformat()
        return _dict
