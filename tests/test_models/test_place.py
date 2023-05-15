#!/usr/bin/python3
'''import modules'''
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    '''unit tests'''
    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
