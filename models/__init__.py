#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv

enviroment = getenv('HBNB_TYPE_STORAGE')

if enviroment == 'db':
    storage = DBStorage()
    storage.reload()

else:
    storage = FileStorage()
    storage.reload()
