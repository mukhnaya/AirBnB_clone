#!/usr/bin/python3
import os
import uuid
from datetime import datetime
'''This is the first moduel'''


class BaseModel:
    '''This is the body of the BaseModel class'''
    def __init__(self, id, created_at, updated_at):
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

        self.id = uuid.uuid4()
        self.id = str(self.id)
        ''' ensure that created_at remains'''
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__():

