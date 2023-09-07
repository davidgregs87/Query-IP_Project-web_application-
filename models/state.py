#!/usr/bin/python3
"""A state module"""

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")
class State(BaseModel, Base):
    """a user class"""
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(60), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)