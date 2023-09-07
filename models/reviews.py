#!/usr/bin/python3
"""a reviews module"""

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")

class Review(BaseModel, Base):
    """a review class"""
    __tablename__ = 'reviews'
    if storage_type == 'db':
        text = Column(String(128), nullable=False)
    else:
        text = ""