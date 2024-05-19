#!/usr/bin/python3
"""This is base model class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel"""
    def __init__(self, *args, **kwargs):
        """init of new BaseModel
        kwargs argument used for for the constructor of a BaseModel

        """
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """ """
        idict = self.__dict__.copy()
        idict["__class__"] = self.__class__.__name__
        idict["created_at"] = self.created_at.isoformat()
        idict["updated_at"] = self.updated_at.isoformat()
        return idict

    def __str__(self):
        """ """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
