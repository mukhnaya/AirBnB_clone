#!/usr/bin/python3
'''import modules'''
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    '''unit tests'''
    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


if __name__ == "__main__":
    unittest.main()
