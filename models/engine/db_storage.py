#!/usr/bin/python3
"""
Database engine
"""

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models import base_model, amenity, city, place, review, state, user


class DBStorage:
    """
    Handles long term storage of all class instances
    """
    CNC = {
        'BaseModel': base_model.BaseModel,
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
    }

    """
    Handles storage for database
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Creates the engine self.__engine
        """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.environ.get('HBNB_MYSQL_USER'),
                os.environ.get('HBNB_MYSQL_PWD'),
                os.environ.get('HBNB_MYSQL_HOST'),
                os.environ.get('HBNB_MYSQL_DB')))
        if os.environ.get("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of all objects
        """
        obj_dict = {}
        if cls:
            obj_class = self.__session.query(self.CNC.get(cls)).all()
            for item in obj_class:
                obj_dict[item.id] = item
            return obj_dict
        for class_name in self.CNC:
            if class_name == 'BaseModel':
                continue
            obj_class = self.__session.query(
                self.CNC.get(class_name)).all()
            for item in obj_class:
                obj_dict[item.id] = item
        return obj_dict

    def new(self, obj):
        """
        Adds objects to current database session
        """
        self.__session.add(obj)
    def all(self, cls=None):
        """
        Returns a dictionary of all objects
        """
        obj_dict = {}
        if cls:
            obj_class = self.__session.query(self.CNC.get(cls)).all()
            for item in obj_class:
                obj_dict[item.id] = item
            return obj_dict
        for class_name in self.CNC:
            if class_name == 'BaseModel':
                continue
            obj_class = self.__session.query(
                self.CNC.get(class_name)).all()
            for item in obj_class:
                obj_dict[item.id] = item
        return obj_dict

    def save(self):
        """
        Commits all changes of current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes obj from current database session if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in database & session from engine
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))

    def close(self):
        """
        Calls remove() on private session attribute (self.session)
        """
        self.__session.remove()

    def get(self, cls, id):
        """
        Retrieves object based on class name and ID
        """
        return(self.all(cls).get(id))

    def count(self, cls=None):
        """
        Count the number of objects in storage
        """
        return (len(self.all(cls)))
