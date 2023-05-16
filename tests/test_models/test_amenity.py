#!/usr/bin/python3
'''test amenity file'''
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''tests'''

    def test_should_create_amenity_instance(self):
        """
            Test amenity
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_shoudl_create_instance_variables(self):
        """
            Test variables
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)
