#!/usr/bin/python3
'''import modules'''
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    '''tests'''
    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))


if __name__ == "__main__":
    unittest.main()
