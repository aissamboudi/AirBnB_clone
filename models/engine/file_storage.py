#!/usr/bin/python3
""" """

import json
from models.base_model import BaseModel


class FileStorage:
    """This is Class of Storage """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Return All Objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """This push a obj in __objects Attribute"""
        item = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[item] = obj

    def save(self):
        """Serialize __objects to __file_path"""
        fs_obj = FileStorage.__objects
        obj_dictionary = {x: fs_obj[x].to_dict() for x in fs_obj.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dictionary, file)

    def reload(self):
        """Deserialize JSON from Filepath to __objects"""
        try:
            with open(FileStorage.__file_path, "r+") as file:
                obj_dictionary = json.load(file)
                for obj in obj_dictionary.values():
                    name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(name)(**obj))
        except FileNotFoundError:
            return
