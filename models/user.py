#!/usr/bin/python3
"""A user module"""

from models.basemodel import BaseModel

class User(BaseModel):
    """a user class"""
    firstname = ""
    lastname = ""
    email = ""
    password = ""
    country = ""
    city = ""
    phone_no = 0
    address = ""