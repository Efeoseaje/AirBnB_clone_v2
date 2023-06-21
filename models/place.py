#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
import models
import os
import sqlalchemy
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship


metadata = Base.metadata
place_amenity = Table(
        'place_amenity',
        metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey('places.id'),
            primary_key=True,
            nullable=False
            ),
        Column(
            'amenity_id',
            String(60),
            ForeignKey('amenities.id'),
            primary_key=True,
            nullable=False
            )
        )
storage_type = os.getenv('HBNB_TYPE_STORAGE')


class Place(BaseModel, Base):
    """Representation of Place """
    if storage_type == 'db':

        __tablename__ = 'places'

        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship(
                "Review",
                cascade="all, delete",
                backref="places"
                )
        amenities = relationship(
                "Amenity",
                secondary=place_amenity,
                viewonly=False,
                backref="places",
                )
    else:
        city_id = str()
        user_id = str()
        name = str()
        description = str()
        number_rooms = int()
        number_bathrooms = int()
        max_guest = int()
        price_by_night = int()
        latitude = float()
        latitude = round(latitude, 1)
        longitude = float()
        amenity_ids = str()

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """attribute that returns list of Review instances"""
        values_review = models.storage.all("Review").values()
        list_review = []
        for review in values_review:
            if review.place_id == self.id:
                list_review.append(review)
        return list_review

    @property
    def amenities(self):
        """attribute that returns list of Amenity instances"""
        values_amenity = models.storage.all("Amenity").values()
        list_amenity = []
        for amenity in values_amenity:
            if amenity.place_id == self.id:
                list_amenity.append(amenity)
        return list_amenity

    @amenities.setter
    def amenitie(self, amenity):
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
