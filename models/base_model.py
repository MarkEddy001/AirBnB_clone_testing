#!/usr/bin/python3
""" A module that contains the BaseModel class that

defines all common attributes/methods for other classes
"""


import uuid
import datetime
from models import storage


class BaseModel:
    """a class that defines all common attributes/methods
        for other classes

    Public instance attributes:
    ---------------------------
    id: string - assign with an uuid.uuid4()
        when an instance is created

    created_at: datetime - assign with the current datetime
                when an instance is created

    updated_at: datetime - assign with the current datetime
    when an instance is created
    it will be updated every time the object is changed

    Public instance methods:
    ------------------------
        save(self):
        updates the public instance attribute
        updated_at with the current datetime
    """

    def __init__(self, *args, **kwargs) -> None:
        """BaseModel object constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.datetime.fromisoformat(value)
                elif key == "updated_at":
                    self.updated_at = datetime.datetime.fromisoformat(value)
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            current_datetime = datetime.datetime.now()
            self.created_at = current_datetime
            self.updated_at = current_datetime
            storage.new(self)

    def __str__(self) -> str:
        """return string representation"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
            )

    def save(self):
        """updates the public instance attribute `updated_at`
        with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        key = self.__class__.__name__ + "." + self.id
        storage._FileStorage__objects[key] = self.to_dict()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__

        a key __class__  will be added to this dictionary
        with the class name of the object

        created_at and updated_at will be converted to string object
        in ISO format:
        %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = datetime.datetime.isoformat(self.created_at)
        new_dict["updated_at"] = datetime.datetime.isoformat(self.updated_at)
        return new_dict
