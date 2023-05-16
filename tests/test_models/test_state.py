#!/usr/bin/python3
'''import modules'''
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState(unittest.TestCase):
    '''unit tests'''
    
    def test_should_create_state_instance(self):
        """
            TestState
        """
        state = State()
        self.assertIsInstance(state, State)

    def test_should_create_state_variable(self):
        """
            TestVariable
        """
        state = State()
        self.assertIsInstance(state.name, str)
