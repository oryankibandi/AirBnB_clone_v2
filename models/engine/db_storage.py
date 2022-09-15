#!/usr/bin/python3
from models.base_model import BaseModel
from models.base_model import Base
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv


class DBStorage:
    """Defines DBStorage"""
    __engine = None
    __session = None

    Session = sessionmaker()

    def __init__(self):
        """Initializes engine"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries all objects on the current database session"""
        if cls is not None:
            return session.query(cls).all()
        else:
            return self.__session.query(User, State, Review,
                                        Place, City, Amenity).all()

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads tables from storage"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=True)
        Session = scoped_session(session_factory)
        self.__engine = Session()
