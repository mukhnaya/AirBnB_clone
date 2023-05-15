#!/usr/bin/python3
'''test amenity file'''
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    '''tests'''
    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))


if __name__ == "__main__":
    unittest.main()
