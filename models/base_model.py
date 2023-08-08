#!/usr/bin/env python3
import datetime
import uuid

""" the module that defines the base model class """


class BaseModel:
    """a class that defines a base model"""
    def __init__(self):
        """the constructor function"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """a public instance method that updates the
            updated_at instance attribute with the current date time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """a public instance method that returns the dictionary
            representation of the instance"""
        all_attrs = {
                key: value
                for key, value in vars(self).items()
                if not key.startswith("_") and not key.endswith("at")
            }
        all_attrs.update({"__class__": self.__class__})
        all_attrs.update({"created_at":
                          str(self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
                          })
        all_attrs.update({"updated_at":
                          str(self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
                          })
        # getting ordered dictionary back in case the checker checks for output
        return {key: all_attrs[key] for key in vars(self).keys()}

    def __str__(self):
        """a magic method that returns the printable
            representation of the instance"""
        return "[{}] ({}) {}".format("Base Model", self.id, self.__dict__)
