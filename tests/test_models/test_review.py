#!/usr/bin/python3
'''import modules'''
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    '''unit tests'''
    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))


if __name__ == "__main__":
    unittest.main()
