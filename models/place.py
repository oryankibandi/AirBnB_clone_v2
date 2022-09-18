#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel
from models.base_model import Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, ForeignKey, Float, Integer, Table
from sqlalchemy.orm import relationship
from os import getenv


table = Table("place_amenity", Base.metadata,
              Column("place_id", String(60),
                     ForeignKey("places.id"),
                     primary_key=True, nullable=False),
              Column("amenity_id", String(60),
                     ForeignKey("amenities.id"),
                     primary_key=True, nullable=False))


class Place(BaseModel, Base):
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
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly="False")
        reviews = relationship("Review", backref="place", cascade='delete')
    else:
        @property
        def reviews(self):
            """Get reviews """
            from models import storage
            reviews = []
            all_reviews = models.storage.all(Review)
            for value in all_reviews.values():
                if value.place_id == self.id:
                    reviews.append(value)
            return reviews

        @property
        def amenities(self):
            """
            """
            amenities = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.id == self.amenity_ids:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
