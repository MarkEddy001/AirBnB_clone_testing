#!/usr/bin/python3
"""Unittest module for the State Class."""

from models.state import State
from models.base_model import BaseModel
import unittest
import datetime


class Test_State(unittest.TestCase):
    """This class contains several methods to the
    the class <State>
    """
    def test_class_name(self):
        """Test if the class belongs to State"""
        s1 = State()
        self.assertEqual(type(s1), State)

    def test_subclass_name(self):
        """Test if the subclass belongs to BaseModel"""
        s1 = State()
        self.assertTrue(issubclass(type(s1), BaseModel))

    def test_obj_attr(self):
        """Test the class attribute of the object"""
        s1 = State()
        self.assertTrue(hasattr(s1, "name"))
        self.assertEqual(s1.name, "")
        self.assertEqual(s1.__dict__.get("name"), None)

    def test_unique_id(self):
        """Test for unique id among instances"""
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)

    def test_string_id(self):
        """Test if the id is a string"""
        s1 = State()
        self.assertEqual(type(s1.id), str)
        s2 = State()
        self.assertEqual(type(s2.id), str)

    def test_created_at(self):
        """Test the created_at attribute"""
        s1 = State()
        self.assertEqual(type(s1.created_at), datetime.datetime)
        self.assertEqual(s1.created_at, s1.updated_at)
        s2 = State()
        self.assertLess(s1.created_at, s2.created_at)

    def test_updated_at(self):
        """Test the updated_at attribute"""
        s1 = State()
        self.assertEqual(type(s1.updated_at), datetime.datetime)
        self.assertEqual(s1.created_at, s1.updated_at)
        s2 = State()
        self.assertLess(s1.updated_at, s2.updated_at)

    def test_str_method(self):
        """Test the string implementation of the instance"""
        s1 = State()
        s1.id = "89"
        s1.name = "Yasmin"
        expected_out = "[State] (89) {}".format(s1.__dict__)
        self.assertEqual(str(s1), expected_out)

    def test_save(self):
        """Test if the updated_at is truly updated"""
        s1 = State()
        temp_updated_at = s1.updated_at
        s1.save()
        self.assertLess(temp_updated_at, s1.updated_at)
        self.assertNotEqual(s1.updated_at, s1.created_at)
        temp_updated_at = s1.updated_at
        s1.save()
        self.assertLess(temp_updated_at, s1.updated_at)

    def test_to_dict(self):
        """Test all the attribute stored in the dictionary"""
        s1 = State()
        obj_dict = s1.to_dict()
        self.assertEqual(type(obj_dict), dict)
        self.assertEqual(obj_dict["__class__"], "State")
        self.assertEqual(type(obj_dict["created_at"]), str)
        self.assertEqual(type(obj_dict["updated_at"]), str)
        convert_isoformat = datetime.datetime.fromisoformat(
            obj_dict["created_at"])
        self.assertEqual(type(convert_isoformat), datetime.datetime)
        convert_isoformat = datetime.datetime.fromisoformat(
            obj_dict["updated_at"])
        self.assertEqual(type(convert_isoformat), datetime.datetime)
        self.assertEqual(s1.id, obj_dict["id"])

# ---------------------------Unittest Task 4-------------------------------

    def test_instantiation_with_kwargs(self):
        """ test creating an instance with kwargs.

        kwargs is a dictionary representation of another object
        """
        s1 = State()
        s1_json = s1.to_dict()
        s2 = State(**s1_json)
        self.assertEqual(type(s2), State)

    def test_no_class_attr_obj_instance_with_kwargs(self):
        """ Checks that obj created with kwargs doesn't have class attribute
        """
        s1 = State()
        s1_json = s1.to_dict()
        s2 = State(**s1_json)
        self.assertNotIn("__class__", s2.__dict__)

    def test_obj_instance_with_kwargs_attr_types_values(self):
        """ Checks that obj created with kwargs has attributes:

        id -> str
        creted_at -> datetime object
        updated_at -> datetime object
        """
        s1 = State()
        s1_json = s1.to_dict()
        s2 = State(**s1_json)
        self.assertEqual(type(s2.id), str)
        self.assertEqual(type(s2.updated_at), datetime.datetime)
        self.assertEqual(type(s2.created_at), datetime.datetime)
        self.assertEqual(s1.id, s2.id)
        self.assertEqual(s1.created_at, s2.created_at)
        self.assertEqual(s1.updated_at, s2.updated_at)

    def test_obj_instance_with_dict_attr(self):
        """ Ensures that obj created with kwargs has the same dictionary
            attribute as the obj created from
        """
        s1 = State()
        s1_json = s1.to_dict()
        s2 = State(**s1_json)
        self.assertEqual(s1.__dict__, s2.__dict__)

        s3 = State()
        s3.name = "my name"
        s3.number = 98
        s3_json = s3.to_dict()
        s4 = State(**s3_json)
        self.assertEqual(s3.__dict__, s4.__dict__)

    def test_two_object_to_dict_return(self):
        """ Ensures that obj created with kwargs has the same dictionary
            retuned by to_dict method as the obj created from
        """
        s1 = State()
        s1_json = s1.to_dict()
        s2 = State(**s1_json)
        self.assertEqual(s2.to_dict(), s1_json)

    def test_two_objects_are_different(self):
        """ Checks that obj created with kwargs is a new object
        """
        s1 = State()
        s1_json = s1.to_dict()
        s2 = State(**s1_json)
        self.assertFalse(s1 is s2)
