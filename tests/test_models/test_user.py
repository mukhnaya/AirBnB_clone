#!/usr/bin/python3
'''import modules'''
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser(unittest.TestCase):
    '''tests'''

    def test_should_create_user_instance(self):
        """
        Test
        """
        user = User()
        self.assertIsInstance(user, User)

    def test_should_creat_user_variables(self):
        """
        Test
        """
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
