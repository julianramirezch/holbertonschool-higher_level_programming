#!/usr/bin/python3
""" Module: 13-student """


class Student:
    """ Class Student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            dict_a = {}
            for key in attrs:
                if hasattr(self, key):
                    dict_a.update({key: getattr(self, key)})
        return dict_a

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if json:
            self.__dict__ = json
