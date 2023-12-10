#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

from models.base_model import BaseModel
import unittest
import datetime


class Test_Base_Model(unittest.TestCase):

    """Test Cases for the BaseModel class."""

    def test_create_instance(self):
        """Check if a new instance is created successfully."""
        b1 = BaseModel()
        self.assertEqual(type(b1), BaseModel)
        # with self.assertRaises(TypeError):
        #     b2 = BaseModel(2)

    def test_unique_id(self):
        """test for unique id among instances"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_string_id(self):
        """Verify that the id is a string type."""
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)
        b2 = BaseModel()
        self.assertEqual(type(b2.id), str)

    def test_created_at(self):
        """Evaluate 'created_at' attribute for proper datetime
        type and equality to 'updated_at'.
        """
        b1 = BaseModel()
        self.assertEqual(type(b1.created_at), datetime.datetime)
        self.assertEqual(b1.created_at, b1.updated_at)
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_updated_at(self):
        """Assess 'updated_at' attribute for correct datetime
        type and ordering between instances.
        """
        b1 = BaseModel()
        self.assertEqual(type(b1.updated_at), datetime.datetime)
        self.assertEqual(b1.created_at, b1.updated_at)
        b2 = BaseModel()
        self.assertLess(b1.updated_at, b2.updated_at)

    def test_str_method(self):
        """Checks the string implementation of the instance"""
        b1 = BaseModel()
        b1.id = "89"
        b1.name = "MarkEddy001"
        expected_out = "[BaseModel] (89) {}".format(b1.__dict__)
        self.assertEqual(str(b1), expected_out)

    def test_save(self):
        """Checks if the updated_at is truly updated"""
        b1 = BaseModel()
        temp_updated_at = b1.updated_at
        b1.save()
        self.assertLess(temp_updated_at, b1.updated_at)
        self.assertNotEqual(b1.updated_at, b1.created_at)
        temp_updated_at = b1.updated_at
        b1.save()
        self.assertLess(temp_updated_at, b1.updated_at)

    def test_to_dict(self):
        """Checks all the attribute stored in the dictionary"""
        b1 = BaseModel()
        obj_dict = b1.to_dict()
        self.assertEqual(type(obj_dict), dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(type(obj_dict["created_at"]), str)
        self.assertEqual(type(obj_dict["updated_at"]), str)
        convert_isoformat = datetime.datetime.fromisoformat(
            obj_dict["created_at"])
        self.assertEqual(type(convert_isoformat), datetime.datetime)
        convert_isoformat = datetime.datetime.fromisoformat(
            obj_dict["updated_at"])
        self.assertEqual(type(convert_isoformat), datetime.datetime)
        self.assertEqual(b1.id, obj_dict["id"])

    # -------------------------Unittest Task 4-------------------------------

    def test_instantiation_with_kwargs(self):
        """Evaluates creating an instance with kwargs.

        kwargs is a dictionary representation of another object
        """
        b1 = BaseModel()
        b1_json = b1.to_dict()
        b2 = BaseModel(**b1_json)
        self.assertEqual(type(b2), BaseModel)

    def test_no_class_attr_obj_instance_with_kwargs(self):
        """Checks that obj created with kwargs doesn't have __class__ attribute"""
        b1 = BaseModel()
        b1_json = b1.to_dict()
        b2 = BaseModel(**b1_json)
        self.assertNotIn("__class__", b2.__dict__)

    def test_obj_instance_with_kwargs_attr_types_values(self):
        """Checks that obj created with kwargs has attributes:

        id -> str
        creted_at -> datetime object
        updated_at -> datetime object
        """
        b1 = BaseModel()
        b1_json = b1.to_dict()
        b2 = BaseModel(**b1_json)
        self.assertEqual(type(b2.id), str)
        self.assertEqual(type(b2.updated_at), datetime.datetime)
        self.assertEqual(type(b2.created_at), datetime.datetime)
        self.assertEqual(b1.id, b2.id)
        self.assertEqual(b1.created_at, b2.created_at)
        self.assertEqual(b1.updated_at, b2.updated_at)

    def test_obj_instance_with_dict_attr(self):
        """Checks that obj created with kwargs has the same dictionary
        attribute as the obj created from
        """
        b1 = BaseModel()
        b1_json = b1.to_dict()
        b2 = BaseModel(**b1_json)
        self.assertEqual(b1.__dict__, b2.__dict__)

        b3 = BaseModel()
        b3.name = "my name"
        b3.number = 98
        b3_json = b3.to_dict()
        b4 = BaseModel(**b3_json)
        self.assertEqual(b3.__dict__, b4.__dict__)

    def test_two_object_to_dict_return(self):
        """Checks that obj created with kwargs has the same dictionary
        retuned by to_dict method as the obj created from
        """
        b1 = BaseModel()
        b1_json = b1.to_dict()
        b2 = BaseModel(**b1_json)
        self.assertEqual(b2.to_dict(), b1_json)

    def test_two_objects_are_different(self):
        """Checks that obj created with kwargs is a new object"""
        b1 = BaseModel()
        b1_json = b1.to_dict()
        b2 = BaseModel(**b1_json)
        self.assertFalse(b1 is b2)
