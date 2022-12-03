#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.schema import Table


place_amenity = Table('place_amenity', Base.metadata,
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), nullable=False, primary_key=True),
                      Column('place_id', String(60),
                             ForeignKey('places.id'), nullable=False, primary_key=True))


if getenv('HBNB_TYPE_STORAGE') == 'db':
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review', backref="place", cascade='delete')
    amenities = relationship('Amenity', secondary=place_amenity,
                             viewonly=False)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref="place", cascade='delete')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    @property
    def amenities(self):
        """ Method for amenities"""
        amenities_list = []
        from models import storage
        dic = storage.all(Amenity)
        if dic:
            for key, val in dic.items():
                if self.id == val.place_id:
                    amenities_list.append(val)
        return amenities_list

    @amenities.setter
    def amenities(self, value):
        """setter method for amenities"""
        if type(value) != Amenity:
            return
        self.amenity_ids.append(value)

    @property
    def reviews(self):
        """ getter method for reviews"""
        reviews_list = []
        from models import storage
        dic = storage.all(Review)
        if dic:
            for key, val in dic.items():
                if self.id == val.place_id:
                    reviews_list.append(val)
        return reviews_list
