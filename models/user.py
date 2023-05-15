#!/usr/bin/python3
""" import modules """
from models.base_model import BaseModel


class User(BaseModel):
    """ inherit from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
