#!/usr/bin/python3
"""A filestorage module"""

import json

class FileStorage:
    """A file storage class that will handle our storage to file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """A method that returns all dictionary objects"""
        return self.__objects
    
    def new(self, obj):
        """A method that sets in __objects the obj with key <obj class name>.id"""
        obj_name = obj.__class__.__name__
        obj_id = obj.id
        obj_key = "{}.{}".format(obj_name, obj_id)
        self.__objects[obj_key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, val in self.__objects.items():
            all_val = val.to_dict()
            new_dict[key] = all_val
        with open(self.__file_path, "w") as file:
            json.dump(new_dict, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists ; otherwise, do nothing. If 
        the file doesnt exist, no exception should be raised)"""
        with open(self.__file_path, "r") as f:
            load_obj = json.load(f)
            from models.basemodel import BaseModel
            from models.user import User
            from models.reviews import Review
            classes = {"BaseModel": BaseModel, "User": User, "Review": Review}
            for key, val in load_obj.items():
                obj_class = key.split('.')[0]
                self.__objects[key] = classes[obj_class](**val)

