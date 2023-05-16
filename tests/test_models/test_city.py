#!/usr/bin/python3
'''import modules'''
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    '''unit tests'''
    
    def test_should_create_intance_of_city(self):
        """
            Test instance creation
        """
        city = City()
        self.assertIsInstance(city, City)

    def test_should_create_instance_variable(self):
        """
            Test variable
        """
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)
