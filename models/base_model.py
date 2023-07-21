#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models
import os

    Base = declarative_base()
storage_type = os.getenv('HBNB_TYPE_STORAGE')


class BaseModel:
    """A base class for all hbnb models"""
    if storage_type == 'db':
        id = Column(String(60), nullable=False, primary_key=True)
        created_at = Column(
                DateTime,
                nullable=False,
                default=datetime.utcnow()
                )
        updated_at = Column(
                DateTime,
                nullable=False,
                default=datetime.utcnow()
                )
    else:
        id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dict = self.__dict__.copy()
        for key, value in dict.items():
            if key == '_sa_instance_state':
                del dict[key]
            if key == 'created_at':
                dict[key] = self.created_at.isoformat()
            if key == 'updated_at':
                dict[key] = self.updated_at.isoformat()
            dict['__class__'] = self.__class__.__name__
        print (dict)
        return dict

    def delete(self):
        ''' deletes the current instance from the storage '''
        models.storage.delete(self)
