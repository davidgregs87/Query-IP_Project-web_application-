#!/usr/bin/python3
"""A module for our basemodel"""

from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from os import getenv

Base = declarative_base()

storage_type = getenv('HBNB_TYPE_STORAGE')

class BaseModel:
    """A basemodel class where all child classes will inherit from"""
    if storage_type == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    
    def __init__(self, *args, **kwargs) -> None:
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            
        else:
            for key, val in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    val = datetime.now()
                if key != '__class__':
                    setattr(self, key, val)

    def save(self) -> datetime:
        """A method that saves the current state with the current time"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()
        storage.new(self)
    
    def __str__(self) -> str:
        """A string representation of our python objects"""
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def to_dict(self) -> dict:
        """A method that returns a dictionary"""
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        return my_dict
    
    def delete(self) -> None:
        """A method that deletes an instance from storage"""
        from models import storage
        storage.delete(self)

  