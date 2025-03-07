#!/usr/bin/python3
"""
DBStorgae
"""
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import os
from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage():
    """
    New Storage
    """

    __engine = None
    __session = None

    def __init__(self):
        """initialize engine"""
        name = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        query = 'mysql+mysqldb://{}:{}@{}/{}'.format(name, pwd, host, db)
        self.__engine = create_engine(query, pool_pre_ping=True)
        env = os.getenv("HBNB_ENV")
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        classes = [Place, State, City, Amenity,
                   Review, User]
        return_dict = {}
        if cls is None:
            for cls_name in classes:
                for obj in self.__session.query(cls_name).all():
                    key = "{}.{}".format(cls_name.__name__, obj.id)
                    return_dict[key] = obj
        else:
            if type(cls) == str:
                cls = eval(cls)

            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__name__, obj.id)
                return_dict[key] = obj
        return return_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary from file"""

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """call remove() method on the session attribute"""
        self.__session.close()
