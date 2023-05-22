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
    def test_should_create_review_instance(self):
        """
            tests
        """
        review = Review()
        self.assertIsInstance(review, Review)

    def test_should_create_instance_variables(self):
        """
            Tests
        """
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)
