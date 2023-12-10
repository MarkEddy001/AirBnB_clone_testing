#!/usr/bin/python3
"""Unittest module for the FileStorage class."""

import json
import unittest
from models.base_model import BaseModel
import os
from models.engine.file_storage import FileStorage
from models import storage


class Test_File_Storage(unittest.TestCase):
    """Test Cases for the FileStorage class."""

    def test_save_to_file(self):
        """Test if the instance is truly save the the file"""
        b1 = BaseModel()
        b1.name = "isiaq"
        b1.save()
        with open("file.json", "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
        self.assertEqual(b1.id, obj_dict["BaseModel" + "." + b1.id]["id"])
        self.assertEqual(b1.to_dict(), obj_dict["BaseModel" + "." + b1.id])

    def test_kwargs_present(self):
        """Test if an instance created with kwargs argument
        present is not saved to the file
        """
        b1 = BaseModel()
        b1.save()
        obj_dict = b1.to_dict()
        b2 = BaseModel(obj_dict)
        b2.save()
        with open("file.json", "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
        get_ret = obj_dict.get("BaseModel" + "." + b2.id).get("id")
        self.assertEqual(get_ret, b2.id)

    def test_raises_exception(self):
        """Test if it raises an exception if the file to save to
        doesn't exist
        """
        if os.path.exists("file.json"):
            os.remove("file.json")
        f1 = FileStorage()
        f1.reload()

    def test_file_storage_attr(self):
        """Test the private attribute of the FileStorage class"""
        f1 = FileStorage()
        with self.assertRaises(AttributeError):
            f1.__file_path
        with self.assertRaises(AttributeError):
            f1.__objects
        self.assertEqual(type(f1._FileStorage__file_path), str)
        self.assertEqual(type(f1._FileStorage__objects), dict)

    def test_storge_instance(self):
        self.assertEqual(type(storage), FileStorage)

    def test_all_dict(self):
        """Test if all the instance stored in the file is returned"""
        b1 = BaseModel()
        b1.save()
        b2 = BaseModel()
        b2.save()
        with open("file.json", "r", encoding="utf-8") as f:
            all_obj = json.load(f)
        self.assertEqual(all_obj, storage.all())
