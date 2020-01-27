#!/usr/bin/python3
""" Module for Base unit tests """
import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def setUp(self):
        """ imports module, instantiates class """
        Base._Base__nb_objects = 0
        pass

    def test_docstring(self):
        """ tests if there is a docstring """
        self.assertIsNotNone(Base.__doc__)

    def tearDown(self):
        """ cleans up after each test_method """
        pass

    def test_if_nb_objects_private(self):
        """ tests if nb_objects is a private class attribute """
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_if_nb_objects_is_initialized(self):
        """ tests if nb_objects initializes to zero """
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_C_instantiation(self):
        '''Tests Base() instantiation.'''
        b = Base()
        self.assertEqual(str(type(b)), "<class 'models.base.Base'>")
        self.assertEqual(b.__dict__, {"id": 1})
        self.assertEqual(b.id, 1)

    

    

if __name__ == "__main__":
    unittest.main()
