#!/usr/bin/python3
"""
This class defines all common attributes/methods for other classes
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:

    def __init__(self):
        """
        Initialization of public instances
        Assign created_at and updated_at attributes with,
        the current datetime when an instance is created
        """

        DATE_AND_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """
        represents the class objects as a string
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
         updates the public instance attribute
         -updated_at- with the current datetime

        """
    def to_dict(self):
        """
        returns a dictionary containing all,
         keys/values of __dict__ of the instance:

        """
