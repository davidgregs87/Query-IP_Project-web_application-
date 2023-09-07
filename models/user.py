#!/usr/bin/python3
"""A user module"""

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

class User(BaseModel, Base):
    """a user class"""
    __tablename__ = 'users'
    if storage_type == 'db':
        user_id = Column(String(60), nullable=False)
        firstname = Column(String(60), nullable=False)
        lastname = Column(String(60), nullable=False)
        email = Column(String(60), nullable=False)
        password = Column(String(60), nullable=False)
        country = Column(String(60), nullable=False)
        city = Column(String(60), nullable=False)
        phone_no = Column(Integer, nullable=False)
        address = Column(String(60), nullable=False)
    else:
        firstname = ""
        lastname = ""
        email = ""
        password = ""
        country = ""
        city = ""
        phone_no = 0
        address = ""
    
    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)