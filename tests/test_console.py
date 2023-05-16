#!/usr/bin/python3
'''import modules'''
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    '''tests'''
    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)


if __name__ == "__main__":
    unittest.main()
