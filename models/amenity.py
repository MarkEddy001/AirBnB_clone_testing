#!/usr/bin/python3
"""Module for the Amenity class that

defines all  attributes/methods for a Amenity object
"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Definition of an Amenity object that
    inherits from BaseModel"""
    name = ""
