#!/usr/bin/python3
"""
Test for storage
"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Test FileStorage Class"""
    def test_instances(self):
        """Instantiation of FileStorage"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        """Test docstrings"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    def test_file_path(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all(self):
        self.assertEqual(dict, type(storage.all()))

    def test_new(self):
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        storage.new(base_model)
        storage.new(user)
        storage.new(state)
        storage.new(place)
        storage.new(city)
        storage.new(amenity)
        storage.new(review)
        self.assertIn("BaseModel." + base_model.id, storage.all().keys())
        self.assertIn(base_model, storage.all().values())
        self.assertIn("User." + user.id, storage.all().keys())
        self.assertIn(user, storage.all().values())
        self.assertIn("State." + state.id, storage.all().keys())
        self.assertIn(state, storage.all().values())
        self.assertIn("Place." + place.id, storage.all().keys())
        self.assertIn(place, storage.all().values())
        self.assertIn("City." + city.id, storage.all().keys())
        self.assertIn(city, storage.all().values())
        self.assertIn("Amenity." + amenity.id, storage.all().keys())
        self.assertIn(amenity, storage.all().values())
        self.assertIn("Review." + review.id, storage.all().keys())
        self.assertIn(review, storage.all().values())

    def test_save(self):
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()

        storage.new(base_model)
        storage.new(user)
        storage.new(state)
        storage.new(place)
        storage.new(city)
        storage.new(amenity)
        storage.new(review)
        storage.save()

        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + base_model.id, save_text)
            self.assertIn("User." + user.id, save_text)
            self.assertIn("State." + state.id, save_text)
            self.assertIn("Place." + place.id, save_text)
            self.assertIn("City." + city.id, save_text)
            self.assertIn("Amenity." + amenity.id, save_text)
            self.assertIn("Review." + review.id, save_text)

    def test_reload(self):
        """
        Tests method: reload (reloads objects from string file)
        """
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)


if __name__ == '__main__':
    unittest.main()
