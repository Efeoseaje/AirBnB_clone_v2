#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = relationship(
            "Place",
            secondary="place_amenity",
            backref="amenities"
            )

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
