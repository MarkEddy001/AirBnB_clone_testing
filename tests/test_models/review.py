#!/usr/bin/python3
"""This module contains the test cases for the class
    <Review>
    """

from models.review import Review
from models.base_model import BaseModel
import unittest
import datetime


class Test_Review(unittest.TestCase):
    """This class contains several methods to the
    the class <Review>
    """
    def test_class_name(self):
        """Test if the class belongs to Review"""
        r1 = Review()
        self.assertEqual(type(r1), Review)

    def test_subclass_name(self):
        """Test if the subclass belongs to BaseModel"""
        r1 = Review()
        self.assertTrue(issubclass(type(r1), BaseModel))

    def test_obj_attr(self):
        """Test the class attribute of the object"""
        r1 = Review()
        self.assertTrue(hasattr(r1, "place_id"))
        self.assertTrue(hasattr(r1, "user_id"))
        self.assertTrue(hasattr(r1, "text"))
        self.assertEqual(r1.place_id, "")
        self.assertEqual(r1.user_id, "")
        self.assertEqual(r1.text, "")
        self.assertEqual(r1.__dict__.get("place_id"), None)
        self.assertEqual(r1.__dict__.get("user_id"), None)
        self.assertEqual(r1.__dict__.get("text"), None)

    def test_unique_id(self):
        """Checks for unique id among instances"""
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)

    def test_string_id(self):
        """Checks if the id is a string"""
        r1 = Review()
        self.assertEqual(type(r1.id), str)
        r2 = Review()
        self.assertEqual(type(r2.id), str)

    def test_created_at(self):
        """Test the created_at attribute"""
        r1 = Review()
        self.assertEqual(type(r1.created_at), datetime.datetime)
        self.assertEqual(r1.created_at, r1.updated_at)
        r2 = Review()
        self.assertLess(r1.created_at, r2.created_at)

    def test_updated_at(self):
        """Test the updated_at attribute"""
        r1 = Review()
        self.assertEqual(type(r1.updated_at), datetime.datetime)
        self.assertEqual(r1.created_at, r1.updated_at)
        r2 = Review()
        self.assertLess(r1.updated_at, r2.updated_at)

    def test_str_method(self):
        """Checks the string implementation of the instance"""
        r1 = Review()
        r1.id = "89"
        r1.name = "MarkEddy001"
        expected_out = "[Review] (89) {}".format(r1.__dict__)
        self.assertEqual(str(r1), expected_out)

    def test_save(self):
        """Test if the updated_at is truly updated"""
        r1 = Review()
        temp_updated_at = r1.updated_at
        r1.save()
        self.assertLess(temp_updated_at, r1.updated_at)
        self.assertNotEqual(r1.updated_at, r1.created_at)
        temp_updated_at = r1.updated_at
        r1.save()
        self.assertLess(temp_updated_at, r1.updated_at)

    def test_to_dict(self):
        """Validate all the attribute stored in the dictionary"""
        r1 = Review()
        obj_dict = r1.to_dict()
        self.assertEqual(type(obj_dict), dict)
        self.assertEqual(obj_dict["__class__"], "Review")
        self.assertEqual(type(obj_dict["created_at"]), str)
        self.assertEqual(type(obj_dict["updated_at"]), str)
        convert_isoformat = datetime.datetime.fromisoformat(
            obj_dict["created_at"])
        self.assertEqual(type(convert_isoformat), datetime.datetime)
        convert_isoformat = datetime.datetime.fromisoformat(
            obj_dict["updated_at"])
        self.assertEqual(type(convert_isoformat), datetime.datetime)
        self.assertEqual(r1.id, obj_dict["id"])

# ---------------------------Unittest Task 4-------------------------------

    def test_instantiation_with_kwargs(self):
        """ Test creating an instance with kwargs.

        kwargs is a dictionary representation of another object
        """
        r1 = Review()
        r1_json = r1.to_dict()
        r2 = Review(**r1_json)
        self.assertEqual(type(r2), Review)

    def test_no_class_attr_obj_instance_with_kwargs(self):
        """ Ensures that obj created with kwargs doesn't have class attribute
        """
        r1 = Review()
        r1_json = r1.to_dict()
        r2 = Review(**r1_json)
        self.assertNotIn("__class__", r2.__dict__)

    def test_obj_instance_with_kwargs_attr_types_values(self):
        """ Checks that obj created with kwargs has attributes:

        id -> str
        creted_at -> datetime object
        updated_at -> datetime object
        """
        r1 = Review()
        r1_json = r1.to_dict()
        r2 = Review(**r1_json)
        self.assertEqual(type(r2.id), str)
        self.assertEqual(type(r2.updated_at), datetime.datetime)
        self.assertEqual(type(r2.created_at), datetime.datetime)
        self.assertEqual(r1.id, r2.id)
        self.assertEqual(r1.created_at, r2.created_at)
        self.assertEqual(r1.updated_at, r2.updated_at)

    def test_obj_instance_with_dict_attr(self):
        """ Ensures that obj created with kwargs has the same dictionary
            attribute as the obj created from
        """
        r1 = Review()
        r1_json = r1.to_dict()
        r2 = Review(**r1_json)
        self.assertEqual(r1.__dict__, r2.__dict__)

        r3 = Review()
        r3.name = "my name"
        r3.number = 98
        r3_json = r3.to_dict()
        r4 = Review(**r3_json)
        self.assertEqual(r3.__dict__, r4.__dict__)

    def test_two_object_to_dict_return(self):
        """ Checks that obj created with kwargs has the same dictionary
            retuned by to_dict method as the obj created from
        """
        r1 = Review()
        r1_json = r1.to_dict()
        r2 = Review(**r1_json)
        self.assertEqual(r2.to_dict(), r1_json)

    def test_two_objects_are_different(self):
        """ Checks that obj created with kwargs is a new object
        """
        r1 = Review()
        r1_json = r1.to_dict()
        r2 = Review(**r1_json)
        self.assertFalse(r1 is r2)
