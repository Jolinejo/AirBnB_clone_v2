#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Table, String, ForeignKey, Float
from sqlalchemy.orm import relationship
import os


place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id')),
    Column('amenity_id', String(60), ForeignKey('amenities.id'))
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place", cascade="all,delete")
        amenities = relationship \
                ("Amenity", secondary=place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            """
            returns the list of Review nstances with
            place_id equals to the current Place.id
            """
            rev = []
            list_of_all = models.storage.all("Review")
            for review in list_of_all:
                if list_of_all[review].place_id == self.id:
                    rev.append(list_of_all[review])
            return rev

        @property
        def amenities(self):
            """amenities list"""
            amen = []
            list_of_all = models.storage.all("Amenity")
            for amenity in list_of_all:
                if list_of_all[amenity].place_id == self.id:
                    amen.append(list_of_all[amenity])
            return amen

        @amenities.setter
        def amenities(self, val):
            """append to list"""
            if val.__class__.__name__ == "Amenity":
                amenity_ids.append(val)

