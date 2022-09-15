#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base import Base
from sqlalchemy import Column, String, ForeignKey, Float, Integer
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ Defines Place class

    Attributes:
        __tablename__ (str): Represents the table name places in MySQL table.
        city_id (String): Represents city's id.
        user_id (String): Represents user's id.
        name (String): Represents user's name.
        description (String): Represents place description
        number_rooms (Integer): number of rooms
        number_bathrooms (Integer): number of bathrooms
        max_guest (Integer): max guest
        price_by_night (Integer): price by night
        latitude (Float): latitude
        longitude (Float): longitude
    """
    __tablename__ = 'places'
    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
