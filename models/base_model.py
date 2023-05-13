#!/usr/bin/python3
import models
import os
import uuid
from datetime import datetime
'''This is the first module'''


class BaseModel:
    '''This is the body of the BaseModel class'''
    def __init__(self, *args, **kwargs):
        '''method to initialize the BaseModel Class'''
        self.id = uuid.uuid4()
        self.id = str(self.id)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        '''updates updated_at variable'''
        self.updated = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns a dictionary 
        containing all keys/values 
        of __dict__ of the instance'''
        base_model_copy = self.__dict__.copy()
        base_model_copy["created_at"] = self.created_at.isoformat()
        base_model_copy["updated_at"] = self.updated_at.isoformat()
        base_model_copy["__class__"] = self.__class__.__name__
        return base_model_copy


    def __str__(self):
        '''output in human readable format'''
        className = self.__class_.__name__
        return className, self.id, self.__dict__
