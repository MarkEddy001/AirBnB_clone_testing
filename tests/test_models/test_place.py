#!/usr/bin/python3
"""This module contains the test cases for the class
    <Place>
    """

from models.place import Place
from models.base_model import BaseModel
import unittest
import datetime


class Test_Place(unittest.TestCase):
    """This class contains several methods to the
    the class <Place>
    """
    def test_class_name(self):
        """Test if the class belongs to Place"""
        p1 = Place()
        self.assertEqual(type(p1), Place)

    def test_subclass_name(self):
        """Test if the subclass belongs to BaseModel"""
        p1 = Place()
        self.assertTrue(issubclass(type(p1), BaseModel))

    def test_obj_attr(self):
        """test the class attribute of the object"""
        p1 = Place()
        self.assertTrue(hasattr(p1, "city_id"))
        self.assertTrue(hasattr(p1, "user_id"))
        self.assertTrue(hasattr(p1, "name"))
        self.assertTrue(hasattr(p1, "description"))
        self.assertTrue(hasattr(p1, "number_rooms"))
        self.assertTrue(hasattr(p1, "number_bathrooms"))
        self.assertTrue(hasattr(p1, "max_guest"))
        self.assertTrue(hasattr(p1, "latitude"))
        self.assertTrue(hasattr(p1, "longitude"))
        self.assertTrue(hasattr(p1, "amenity_ids"))
        self.assertTrue(hasattr(p1, "price_by_night"))
        self.assertEqual(p1.city_id, "")
        self.assertEqual(p1.user_id, "")
        self.assertEqual(p1.name, "")
        self.assertEqual(p1.description, "")
        self.assertEqual(p1.number_rooms, 0)
        self.assertEqual(p1.number_bathrooms, 0)
        self.assertEqual(p1.max_guest, 0)
        self.assertEqual(p1.price_by_night, 0)
        self.assertEqual(p1.latitude, 0.0)
        self.assertEqual(p1.longitude, 0.0)
        self.assertEqual(p1.amenity_ids, [])
        self.assertEqual(p1.__dict__.get("city_id"), None)
        self.assertEqual(p1.__dict__.get("user_id"), None)
        self.assertEqual(p1.__dict__.get("name"), None)
        self.assertEqual(p1.__dict__.get("description"), None)
        self.assertEqual(p1.__dict__.get("number_rooms"), None)
        self.assertEqual(p1.__dict__.get("number_bathrooms"), None)
        self.assertEqual(p1.__dict__.get("max_guest"), None)
        self.assertEqual(p1.__dict__.get("price_by_night"), None)
        self.assertEqual(p1.__dict__.get("latitude"), None)
        self.assertEqual(p1.__dict__.get("longitude"), None)
        self.assertEqual(p1.__dict__.get("amenity_ids"), None)

    def test_unique_id(self):
        """Confirm for unique id among instances"""
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    def test_string_id(self):
        """test if the id is a string"""
        p1 = Place()
        self.assertEqual(type(p1.id), str)
        p2 = Place()
        self.assertEqual(type(p2.id), str)

    def test_created_at(self):
        """Validate the created_at attribute"""
        p1 = Place()
        self.assertEqual(type(p1.created_at), datetime.datetime)
        self.assertEqual(p1.created_at, p1.updated_at)
        p2 = Place()
        self.assertLess(p1.created_at, p2.created_at)

    def test_updated_at(self):
        """Assert the updated_at attribute"""
        p1 = Place()
        self.assertEqual(type(p1.updated_at), datetime.datetime)
        self.assertEqual(p1.created_at, p1.updated_at)
        p2 = Place()
        self.assertLess(p1.updated_at, p2.updated_at)

    def test_str_method(self):
        """Test the custom string implementation of the instance"""
        p1 = Place()
        p1.id = "89"
        p1.name = "Yasmin"
        expected_out = "[Place] (89) {}".format(p1.__dict__)
        self.assertEqual(str(p1), expected_out)

    def test_save(self):
        """Verify that the updated_at is truly updated"""
        p1 = Place()
        temp_updated_at = p1.updated_at
        p1.save()
        self.assertLess(temp_updated_at, p1.updated_at)
        self.assertNotEqual(p1.updated_at, p1.created_at)
        temp_updated_at = p1.updated_at
        p1.save()
        self.assertLess(temp_updated_at, p1.updated_at)

    def test_to_dict(self):
        """test all the attribute stored in the dictionary"""
        p1 = Place()
        obj_dict = p1.to_dict()
        self.assertEqual(type(obj_dict), dict)
        self.assertEqual(obj_dict["__class__"], "Place")
        self.assertEqual(type(obj_dict["created_at"]), str)
        self.assertEqual(type(obj_dict["updated_at"]), str)
        convert_isoformat = datetime.datetime.fromisoformat(
            obj_dict["created_at"])
        self.assertEqual(type(convert_isoformat), datetime.datetime)
        convert_isoformat = datetime.datetime.fromisoformat(
            obj_dict["updated_at"])
        self.assertEqual(type(convert_isoformat), datetime.datetime)
        self.assertEqual(p1.id, obj_dict["id"])

# ---------------------------Unittest Task 4-------------------------------

    def test_instantiation_with_kwargs(self):
        """ test creating an instance with kwargs.

        kwargs is a dictionary representation of another object
        """
        p1 = Place()
        p1_json = p1.to_dict()
        p2 = Place(**p1_json)
        self.assertEqual(type(p2), Place)

    def test_no_class_attr_obj_instance_with_kwargs(self):
        """ Ensures that obj created with kwargs doesn't have class attribute
        """
        p1 = Place()
        p1_json = p1.to_dict()
        p2 = Place(**p1_json)
        self.assertNotIn("__class__", p2.__dict__)

    def test_obj_instance_with_kwargs_attr_types_values(self):
        """ Ensures that obj created with kwargs has attributes:

        id -> str
        creted_at -> datetime object
        updated_at -> datetime object
        """
        p1 = Place()
        p1_json = p1.to_dict()
        p2 = Place(**p1_json)
        self.assertEqual(type(p2.id), str)
        self.assertEqual(type(p2.updated_at), datetime.datetime)
        self.assertEqual(type(p2.created_at), datetime.datetime)
        self.assertEqual(p1.id, p2.id)
        self.assertEqual(p1.created_at, p2.created_at)
        self.assertEqual(p1.updated_at, p2.updated_at)

    def test_obj_instance_with_dict_attr(self):
        """ Checks that obj created with kwargs has the same dictionary
            attribute as the obj created from
        """
        p1 = Place()
        p1_json = p1.to_dict()
        p2 = Place(**p1_json)
        self.assertEqual(p1.__dict__, p2.__dict__)

        p3 = Place()
        p3.name = "my name"
        p3.number = 98
        p3_json = p3.to_dict()
        p4 = Place(**p3_json)
        self.assertEqual(p3.__dict__, p4.__dict__)

    def test_two_object_to_dict_return(self):
        """ Checks that obj created with kwargs has the same dictionary
            retuned by to_dict method as the obj created from
        """
        p1 = Place()
        p1_json = p1.to_dict()
        p2 = Place(**p1_json)
        self.assertEqual(p2.to_dict(), p1_json)

    def test_two_objects_are_different(self):
        """ Checks that obj created with kwargs is a new object
        """
        p1 = Place()
        p1_json = p1.to_dict()
        p2 = Place(**p1_json)
        self.assertFalse(p1 is p2)
