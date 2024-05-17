#!/usr/bin/python3
""" """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
