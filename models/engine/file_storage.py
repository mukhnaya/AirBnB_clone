#!/usr/bin/python3
'''importing modules '''
import os
from datetime import datetime
import uuid
import json
from .models.base_model import BaseModel


'''class FileStorage'''
class FileStorage:
    '''body of FileStorage Class'''
    __file_path = "file.json"
    __objects = {}

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
            update_dic = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        json.dump(updated_dic, pau)

    def reload(self):
        '''deserializes the JSON file 
        to __objects (only if 
        the JSON file (__file_path) exists ; 
        otherwise, do nothing. 
        If the file doesn’t exist, 
        no exception should be raised)'''
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as pau:
                to_object = json.load(pau)
                for keys, values in to_object.items():
                    FileStorage.__objects[keys] = eval(values['__class__'])(**values)
