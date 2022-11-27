#!/usr/bin/python3
"""Unittest module for the Review Class."""

from datetime import datetime
import json
import os
import re
import time
import unittest
import uuid
from models import storage
from models.review import Review
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Test Cases for the Review class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down tests."""
        self.clear_db()
        pass

    def clear_db(self):
        """Clear FileStorage data and remove local file."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_1_instantiation(self):
        """Tests instantiation of Review class."""

        b = Review()
        self.assertEqual(str(type(b)), "<class 'models.review.Review'>")
        self.assertIsInstance(b, Review)
        self.assertTrue(issubclass(type(b), Review))

    def test_1_init_no_args(self):
        """Tests __init__ with no arguments."""
        self.clear_db()
        with self.assertRaises(TypeError) as e:
            Review.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_1_init_many_args(self):
        """Tests __init__ with many arguments."""
        self.clear_db()
        Review(*[i for i in range(800)])
        Review(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

    def test_1_attributes(self):
        """Tests attributes value for instance of a Amenity class."""

        attrs = storage.attrs()["Review"]
        o = Review()
        for k, v in attrs.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

    def test_1_datetime_created(self):
        """Tests if updated_at and created_at are current at creation."""
        date_now = datetime.now()
        b = Review()
        diff = b.updated_at - b.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = b.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_1_id_unique(self):
        """Tests for unique model ids."""

        a = [Review().id for i in range(1000)]
        self.assertEqual(len(set(a)), len(a))

    def test_1_save(self):
        """Tests that the save() method updates the `updated_at` attr
        of the model"""

        b = Review()
        time.sleep(0.5)
        date_now = datetime.now()
        b.save()
        diff = b.updated_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_1_str(self):
        """Tests for __str__ method."""
        b = Review()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(b))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "Review")
        self.assertEqual(res.group(2), b.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        d2 = b.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)

    def test_1_to_dict(self):
        """Tests the public instance method to_dict()."""

        b = Review()
        b.place_id = "NRB"
        b.user_id = "PO"
        b.text = "Africa's gem"
        d = b.to_dict()
        self.assertEqual(d["id"], b.id)
        self.assertEqual(d["__class__"], type(b).__name__)
        self.assertEqual(d["created_at"], b.created_at.isoformat())
        self.assertEqual(d["updated_at"], b.updated_at.isoformat())
        self.assertEqual(d["text"], b.text)

    def test_1_to_dict_no_args(self):
        """Tests to_dict() with no arguments."""
        self.clear_db()
        with self.assertRaises(TypeError) as e:
            Review.to_dict()
        msg = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_1_to_dict_excess_args(self):
        """Tests to_dict() with too many arguments."""
        self.clear_db()
        with self.assertRaises(TypeError) as e:
            Review.to_dict(self, 15)
        msg = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)

    def test_1_to_dict_excess_args_extra(self):
        """Tests to_dict() with too many arguments."""
        self.clear_db()
        with self.assertRaises(TypeError) as e:
            Review.to_dict(self, 15, None)
        msg = "to_dict() takes 1 positional argument but 3 were given"
        self.assertEqual(str(e.exception), msg)

    def test_2_instantiation(self):
        """Tests instantiation with **kwargs."""

        my_model = Review()
        my_model.place_id = "NRB"
        my_model.user_id = "PO"
        my_model.text = "Africa's gem"
        my_model_json = my_model.to_dict()
        new_model = Review(**my_model_json)
        self.assertEqual(new_model.to_dict(), my_model.to_dict())

    def test_2_instantiation_dict(self):
        """Tests rehydration with **kwargs from custom dict."""
        _dict = {
            "__class__": "Review",
            "updated_at":
                datetime(2022, 11, 26, 23, 11, 59, 56789).isoformat(),
            "created_at": datetime.now().isoformat(),
            "id": uuid.uuid4(),
            "place_id": "NRB",
            "user_id": "PO",
            "text": "Africa's gem"
        }
        m = Review(**_dict)
        self.assertEqual(m.to_dict(), _dict)

    def test_3_save(self):
        """Tests that storage.save() is called from save()."""
        self.clear_db()
        b = Review()
        b.save()
        key = "{}.{}".format(type(b).__name__, b.id)
        d = {key: b.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path, "r", encoding="utf-8") \
                as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

    def test_3_save_no_args(self):
        """Tests save() with no arguments."""
        self.clear_db()
        with self.assertRaises(TypeError) as e:
            Review.save()
        msg = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_3_save_excess_args(self):
        """Tests save() with too many arguments."""
        self.clear_db()
        with self.assertRaises(TypeError) as e:
            Review.save(self, 100)
        msg = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unittest.main()
