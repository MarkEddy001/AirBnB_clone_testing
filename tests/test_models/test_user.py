#!/usr/bin/python3
"""Unittest module for the User Class."""

from models.user import User
from models.base_model import BaseModel
import unittest
import datetime


class Test_User(unittest.TestCase):
    """Test Cases for the User class."""

    def test_class_name(self):
        """Checks if the class belongs to User"""
        u1 = User()
        self.assertEqual(type(u1), User)

    def test_subclass_name(self):
        """Checks if the subclass belongs to BaseModel"""
        u1 = User()
        self.assertTrue(issubclass(type(u1), BaseModel))

    def test_obj_attr(self):
        """Checks the class attribute of the object"""
        u1 = User()
        self.assertTrue(hasattr(u1, "email"))
        self.assertTrue(hasattr(u1, "password"))
        self.assertTrue(hasattr(u1, "first_name"))
        self.assertTrue(hasattr(u1, "last_name"))
        self.assertEqual(u1.email, "")
        self.assertEqual(u1.password, "")
        self.assertEqual(u1.first_name, "")
        self.assertEqual(u1.last_name, "")
        self.assertEqual(u1.__dict__.get("email"), None)
        self.assertEqual(u1.__dict__.get("password"), None)
        self.assertEqual(u1.__dict__.get("first_name"), None)
        self.assertEqual(u1.__dict__.get("last_name"), None)

    def test_unique_id(self):
        """Checks for unique id among instances"""
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    def test_string_id(self):
        """Checks if the id is a string"""
        u1 = User()
        self.assertEqual(type(u1.id), str)
        u2 = User()
        self.assertEqual(type(u2.id), str)

    def test_created_at(self):
        """Checks the created_at attribute"""
        u1 = User()
        self.assertEqual(type(u1.created_at), datetime.datetime)
        self.assertEqual(u1.created_at, u1.updated_at)
        u2 = User()
        self.assertLess(u1.created_at, u2.created_at)

    def test_updated_at(self):
        """Test the updated_at attribute"""
        u1 = User()
        self.assertEqual(type(u1.updated_at), datetime.datetime)
        self.assertEqual(u1.created_at, u1.updated_at)
        u2 = User()
        self.assertLess(u1.updated_at, u2.updated_at)

    def test_str_method(self):
        """Test the string implementation of the instance"""
        u1 = User()
        u1.id = "89"
        u1.name = "Yasmin"
        expected_out = "[User] (89) {}".format(u1.__dict__)
        self.assertEqual(str(u1), expected_out)

    def test_save(self):
        """Test if the updated_at is truly updated"""
        u1 = User()
        temp_updated_at = u1.updated_at
        u1.save()
        self.assertLess(temp_updated_at, u1.updated_at)
        self.assertNotEqual(u1.updated_at, u1.created_at)
        temp_updated_at = u1.updated_at
        u1.save()
        self.assertLess(temp_updated_at, u1.updated_at)

    def test_to_dict(self):
        """Test all the attribute stored in the dictionary"""
        u1 = User()
        obj_dict = u1.to_dict()
        self.assertEqual(type(obj_dict), dict)
        self.assertEqual(obj_dict["__class__"], "User")
        self.assertEqual(type(obj_dict["created_at"]), str)
        self.assertEqual(type(obj_dict["updated_at"]), str)
        convert_isoformat = datetime.datetime.fromisoformat(
            obj_dict["created_at"])
        self.assertEqual(type(convert_isoformat), datetime.datetime)
        convert_isoformat = datetime.datetime.fromisoformat(
            obj_dict["updated_at"])
        self.assertEqual(type(convert_isoformat), datetime.datetime)
        self.assertEqual(u1.id, obj_dict["id"])

# ---------------------------Unittest Task 4-------------------------------

    def test_instantiation_with_kwargs(self):
        """ Test creating an instance with kwargs.

        kwargs is a dictionary representation of another object
        """
        u1 = User()
        u1_json = u1.to_dict()
        u2 = User(**u1_json)
        self.assertEqual(type(u2), User)

    def test_no_class_attr_obj_instance_with_kwargs(self):
        """ Checks that obj created with kwargs doesn't have class attribute
        """
        u1 = User()
        u1_json = u1.to_dict()
        u2 = User(**u1_json)
        self.assertNotIn("__class__", u2.__dict__)

    def test_obj_instance_with_kwargs_attr_types_values(self):
        """ Checks that obj created with kwargs has attributes:

        id -> str
        creted_at -> datetime object
        updated_at -> datetime object
        """
        u1 = User()
        u1_json = u1.to_dict()
        u2 = User(**u1_json)
        self.assertEqual(type(u2.id), str)
        self.assertEqual(type(u2.updated_at), datetime.datetime)
        self.assertEqual(type(u2.created_at), datetime.datetime)
        self.assertEqual(u1.id, u2.id)
        self.assertEqual(u1.created_at, u2.created_at)
        self.assertEqual(u1.updated_at, u2.updated_at)

    def test_obj_instance_with_dict_attr(self):
        """ Checks that obj created with kwargs has the same dictionary
            attribute as the obj created from
        """
        u1 = User()
        u1_json = u1.to_dict()
        u2 = User(**u1_json)
        self.assertEqual(u1.__dict__, u2.__dict__)

        u3 = User()
        u3.name = "my name"
        u3.number = 98
        u3_json = u3.to_dict()
        u4 = User(**u3_json)
        self.assertEqual(u3.__dict__, u4.__dict__)

    def test_two_object_to_dict_return(self):
        """ Checks that obj created with kwargs has the same dictionary
            retuned by to_dict method as the obj created from
        """
        u1 = User()
        u1_json = u1.to_dict()
        u2 = User(**u1_json)
        self.assertEqual(u2.to_dict(), u1_json)

    def test_two_objects_are_different(self):
        """ Checks that obj created with kwargs is a new object
        """
        u1 = User()
        u1_json = u1.to_dict()
        u2 = User(**u1_json)
        self.assertFalse(u1 is u2)
