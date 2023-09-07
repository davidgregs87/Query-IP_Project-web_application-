#!/usr/bin/python3
"""A module for unique instance"""
from models.engine.filestorage import FileStorage
from models.engine.dbstorage import DBStorage
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()