#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


storage_type = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    if storage_type == 'db':
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        cities = relationship(
                "City",
                cascade='all, delete, delete-orphan',
                backref="state"
                )
    else:
        name = str()

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    @property
    def cities(self):
        import models

        cities = []
        all_cities = models.storage.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                cities.append(city)
        return (cities)
