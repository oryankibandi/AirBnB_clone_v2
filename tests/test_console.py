#!/usr/bin/python3
"""Defines unittests for console.py."""
import os
import pep8
import unittest
import models
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


class TestHBNBCommand(unittest.TestCase):
    """Test
    """
    @classsmethod
    def setUpClass(cls):
        """Test set up
        """
        try:
            os.rename("file.json", "make")
        except IOError:
            pass
        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Test
        """
        try:
            os.rename("make", "file.json")
        except IOError:
            pass
        del cls.HBNB


if __name__ == "__main__":
    unittest.main()
