#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

storage_type = getenv('HBNB_TYPE_STORAGE')


class Review(BaseModel, Base):
    """Representation of Review """
    if storage_type == 'db':
        __tablename__ = 'reviews'

        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        place_id = str()
        user_id = str()
        text = str()

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
