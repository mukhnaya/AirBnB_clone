#!/usr/bin/python3
'''import modules'''
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    '''tests'''
    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
