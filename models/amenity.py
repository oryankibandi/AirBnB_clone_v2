#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Defines the Amenities class
    Attributes:
        __tablename__:(str):name of  MySQL table
        name (String): name of amenity
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary='place_amenity',
                                   back_populates="_amenities")
