#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from models.place import Place
from models.review import Review
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes

    Attributes:
        __tablename__ (str): Represents the table name users in MySQL table
        email (String): user's email
        password (String): user's password
        first_name (String): user's first_name
        last_name (String): user's last_name
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user", cascade="all,delete")
    reviews = relationship("Review", backref="user", cascade="all,delete")
