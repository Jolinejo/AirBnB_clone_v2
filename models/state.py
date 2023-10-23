#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import os
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="State", cascade="all,delete")
    else:
        @property
        def cities(self):
            """
            returns the list of City instances with
            state_id equals to the current State.id
            """
            cit = []
            list_of_all = models.storage.all("City")
            for city in list_of_all:
                if list_of_all[city].state_id == self.id:
                    cit.append(list_of_all[city])
            return cit
