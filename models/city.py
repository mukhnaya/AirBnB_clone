#!/usr/bin/python3
""" import modules """
from models.base_model import BaseModel


class City(BaseModel):
    """ City inherits BaseModel """
    state_id = ""
    name = ""
