#!/usr/bin/python3
'''importing modules '''
import os
from os import path
from datetime import datetime
import uuid
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''body of FileStorage Class'''
    __file_path = "file.json"
    __objects = {}

    classes = {"BaseModel": BaseModel,
               "User": User,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Place": Place,
               "Review": Review}

    def all(self):
        '''returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        mos = str(obj.id)
        valarie = obj.__class__.__name__
        FileStorage.__objects[valarie + "." + mos] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as pau:
            update_dic = {key: obj.to_dict() for key, obj in
                          FileStorage.__objects.items()}
            json.dump(update_dic, pau)

    def reload(self):
        '''deserializes the JSON file
        to __objects (only if
        the JSON file (__file_path) exists;
        otherwise, do nothing.
        If the file doesn’t exist,
        no exception should be raised)'''
        if path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                obj = json.load(f)
                dct = {}
                for k, v in obj.items():
                    dct[k] = self.classes[v["__class__"]](**v)
                FileStorage.__objects = dct
        else:
            return
