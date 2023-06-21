#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if storage_type == 'db':
        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)
        place_amenities = relationship(
                "Place",
                secondary="place_amenity",
                backref="amenities"
                )
    else:
        name = str()

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
