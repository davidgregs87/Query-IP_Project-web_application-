#!/usr/bin/python3
"""A module for our basemodel"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A basemodel class where all child classes will inherit from"""
    def __init__(self, *args, **kwargs) -> None:
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)
        else:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.now()
                if key != '__class__':
                    setattr(self, key, val)

    def save(self) -> datetime:
        """A method that saves the current state with the current time"""
        from models import storage
        storage.save()
        self.updated_at = datetime.now()
    
    def __str__(self) -> str:
        """A string representation of our python objects"""
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def to_dict(self) -> dict:
        """A method that returns a dictionary"""
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

  