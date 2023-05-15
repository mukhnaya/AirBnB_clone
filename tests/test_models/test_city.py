#!/usr/bin/python3
'''import modules'''
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    '''unit tests'''
    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))


if __name__ == "__main__":
    unittest.main()
