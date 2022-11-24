#!/usr/bin/python3
"""
Module: FileStorage
"""
import os
import json


class FileStorage(object):
    """
    Class Name: FileStorage
    Description: abstracted storage engine
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """gets all the objects as a dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets new obj in __objects dictionary."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """writes serialized `__objects` to the JSON file."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        return {
            'BaseModel': BaseModel, 'User': User, 'State': State,
            'City': City, 'Place': Place, 'Amenity': Amenity,
            'Review': Review
        }

    def reload(self):
        """Deserializes JSON file into __objects."""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            _obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in _obj_dict.items()}
            FileStorage.__objects = obj_dict
