#!/usr/bin/python3
""" Class city """
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """ The city class attributes  contains state ID and name plus places """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    state = relationship('State')
    places = relationship('Place', cascade="delete")
    in_storage = os.environ.get('HBNB_TYPE_STORAGE')
    if in_storage == 'db':
        state = relationship("State", backref="cities")
