#!/usr/bin/python3
"""class User"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel):
    """Defines a user by various attributes"""
    __tablename__ = 'users'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', cascade='all, delete, delete-orphan')
        reviews = relationship('Review', cascade='delete')
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
