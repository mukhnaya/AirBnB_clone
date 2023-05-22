#!/usr/bin/python3
'''import modules'''
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    '''unit tests'''
    
    def test_instance_storage_form_FileStorage(self):
        """
            Test
        """
        self.assertIsInstance(storage, FileStorage)

    def test_objects_should_be_dictionary(self):
        """
            Test
        """
        s = storage.all()
        self.assertIsInstance(s, dict)

    def test_file_path_instance(self):
        """
        Test raise error
        """
        with self.assertRaises(AttributeError):
            f = FileStorage.__file_path

    def test_objects_for_private(self):
        """
        Test
        """
        f = FileStorage._FileStorage__objects
        self.assertIsInstance(f, dict)

    def test_objects_instance(self):
        """
        Test raise error
        """
        with self.assertRaises(AttributeError):
            f = FileStorage.__objects

    def test_file_path_for_private(self):
        """
        Test
        """
        f = FileStorage._FileStorage__file_path
        self.assertIsInstance(f, str)

    def test_all_method(self):
        """
        Test all method
        """
        d = storage.all()
        self.assertIsInstance(d, dict)

    def test_new_method(self):
        """
        Test new method
        """
        obj = BaseModel()
        storage.new(obj)
        v = "BaseModel.{}".format(obj.id)
        self.assertIn(v, storage.all().keys())

    def test_save_method(self):
        """
        Test save
        """
        storage.save()
        size1 = os.path.getsize(FileStorage._FileStorage__file_path)
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        size2 = os.path.getsize(FileStorage._FileStorage__file_path)
        self.assertNotEqual(size1, size2)

    def test_reload_method(self):
        """
        Test reload
        """
        size1 = len(FileStorage._FileStorage__objects)
        storage.reload()
        size2 = len(FileStorage._FileStorage__objects)
        self.assertNotEqual(size1, size2)

    def test_save_from_save_model(self):
        """
        Test BaseModel.save()
        """
        b = BaseModel()
        u_at = b.updated_at
        uu_at = datetime.now()
        self.assertNotEqual(u_at, uu_at)
