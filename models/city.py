#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlachemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name

    Attributes:
        __tablename__(str): cities table in MySQLdb
        state_id(String): the state id
        name(String): the state name
    """
    __tablename__ = 'cities'
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
