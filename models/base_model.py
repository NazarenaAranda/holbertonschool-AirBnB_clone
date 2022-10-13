#!/usr/bin/python3
"""
	BaseModel MODULE Romina
"""


import json
import uuid
import datetime
import models


class BaseModel:
    """ This will be define all common attributes/methods 
    for other classes """

    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0 and kwargs is not None: # si existen keyword arguments y no son 0
            for key, value in kwargs.items(): #buscando en las kword para identificar si es id, created_at, upadated_at, __class__ o setattr
                if key == "id":
                    self.id = value 
                elif key == __class__:
                    pass
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, %Y-%m-%dT%H:%M:%S.%f) #strptime() to create a datetime object from the string.
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, %Y-%m-%dT%H:%M:%S.%f)
                else:
                    setattr(self, key, value) #le setea un valor si no es ninuno de los casos anteriores
        else:
            self.id = str(uuid)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def to_dict(self):
        """ This will be return a dictionary that contains
        key and values in __dic__ of the instance """
        dicnew = self.__dict__.copy()
        dicnew["created_at"] = self.created_at.isoformat()
        dicnew["updated_at"] = self.updated_at.isoformat()
        dicnew["__class__"] = self.__clas__.__name__
        return newdic
    
    def save(self):
        """ this is useful when you update and has the current time """
        self.udated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """ String rep of the model """
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)
