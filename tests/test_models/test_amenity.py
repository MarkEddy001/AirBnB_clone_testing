#!/usr/bin/python3
"""This module contains Unittest test modules for the Amenity Class."""

from models.amenity import Amenity
from models.base_model import BaseModel
import unittest
import datetime


class Test_Amenity(unittest.TestCase):
    """Test Cases for the Amenity class."""

    def test_class_name(self):
        """test if the class belongs to Amenity"""
        a1 = Amenity()
        self.assertEqual(type(a1), Amenity)

    def test_subclass_name(self):
        """Checks if the subclass belongs to BaseModel"""
        a1 = Amenity()
        self.assertTrue(issubclass(type(a1), BaseModel))

    def test_obj_attr(self):
        """Checks if the object has the 'name' attribute."""
        a1 = Amenity()
        self.assertTrue(hasattr(a1, "name"))
        self.assertEqual(a1.name, "")
        self.assertEqual(a1.__dict__.get("name"), None)

    def test_unique_id(self):
        """test for unique id among instances"""
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

    def test_string_id(self):
        """Checks if the id is a string"""
        a1 = Amenity()
        self.assertEqual(type(a1.id), str)
        a2 = Amenity()
        self.assertEqual(type(a2.id), str)

    def test_created_at(self):
        """Checks the created_at attribute"""
        a1 = Amenity()
        self.assertEqual(type(a1.created_at), datetime.datetime)
        self.assertEqual(a1.created_at, a1.updated_at)
        a2 = Amenity()
        self.assertLess(a1.created_at, a2.created_at)

    def test_updated_at(self):
        """Checks the updated_at attribute"""
        a1 = Amenity()
        self.assertEqual(type(a1.updated_at), datetime.datetime)
        self.assertEqual(a1.created_at, a1.updated_at)
        a2 = Amenity()
        self.assertLess(a1.updated_at, a2.updated_at)

    def test_str_method(self):
        """Checks the string implementation of the instance"""
        a1 = Amenity()
        a1.id = "89"
        a1.name = "MarkEddy001"
        expected_out = "[Amenity] (89) {}".format(a1.__dict__)
        self.assertEqual(str(a1), expected_out)

    def test_save(self):
        """test if the updated_at is truly updated"""
        a1 = Amenity()
        temp_updated_at = a1.updated_at
        a1.save()
        self.assertLess(temp_updated_at, a1.updated_at)
        self.assertNotEqual(a1.updated_at, a1.created_at)
        temp_updated_at = a1.updated_at
        a1.save()
        self.assertLess(temp_updated_at, a1.updated_at)

    def test_to_dict(self):
        """test all the attribute stored in the dictionary"""
        a1 = Amenity()
        obj_dict = a1.to_dict()
        self.assertEqual(type(obj_dict), dict)
        self.assertEqual(obj_dict["__class__"], "Amenity")
        self.assertEqual(type(obj_dict["created_at"]), str)
        self.assertEqual(type(obj_dict["updated_at"]), str)
        convert_isoformat = datetime.datetime.fromisoformat(
            obj_dict["created_at"])
        self.assertEqual(type(convert_isoformat), datetime.datetime)
        convert_isoformat = datetime.datetime.fromisoformat(
            obj_dict["updated_at"])
        self.assertEqual(type(convert_isoformat), datetime.datetime)
        self.assertEqual(a1.id, obj_dict["id"])

# ---------------------------Unittest Task 4-------------------------------

    def test_instantiation_with_kwargs(self):
        """ test creating an instance with kwargs.

        kwargs is a dictionary representation of another object
        """
        a1 = Amenity()
        a1_json = a1.to_dict()
        a2 = Amenity(**a1_json)
        self.assertEqual(type(a2), Amenity)

    def test_no_class_attr_obj_instance_with_kwargs(self):
        """ check that obj created with kwargs doesn't have class attribute
        """
        a1 = Amenity()
        a1_json = a1.to_dict()
        a2 = Amenity(**a1_json)
        self.assertNotIn("__class__", a2.__dict__)

    def test_obj_instance_with_kwargs_attr_types_values(self):
        """ check that obj created with kwargs has attributes:

        id -> str
        creted_at -> datetime object
        updated_at -> datetime object
        """
        a1 = Amenity()
        a1_json = a1.to_dict()
        a2 = Amenity(**a1_json)
        self.assertEqual(type(a2.id), str)
        self.assertEqual(type(a2.updated_at), datetime.datetime)
        self.assertEqual(type(a2.created_at), datetime.datetime)
        self.assertEqual(a1.id, a2.id)
        self.assertEqual(a1.created_at, a2.created_at)
        self.assertEqual(a1.updated_at, a2.updated_at)

    def test_obj_instance_with_dict_attr(self):
        """ check that obj created with kwargs has the same dictionary
            attribute as the obj created from
        """
        a1 = Amenity()
        a1_json = a1.to_dict()
        a2 = Amenity(**a1_json)
        self.assertEqual(a1.__dict__, a2.__dict__)

        a3 = Amenity()
        a3.name = "my name"
        a3.number = 98
        a3_json = a3.to_dict()
        a4 = Amenity(**a3_json)
        self.assertEqual(a3.__dict__, a4.__dict__)

    def test_two_object_to_dict_return(self):
        """ check that obj created with kwargs has the same dictionary
            retuned by to_dict method as the obj created from
        """
        a1 = Amenity()
        a1_json = a1.to_dict()
        a2 = Amenity(**a1_json)
        self.assertEqual(a2.to_dict(), a1_json)

    def test_two_objects_are_different(self):
        """ check that obj created with kwargs is a new object
        """
        a1 = Amenity()
        a1_json = a1.to_dict()
        a2 = Amenity(**a1_json)
        self.assertFalse(a1 is a2)
