#!/usr/bin/python3
""" Module: 6-base_geometry - Class BaseGeometry
    Public instance method:
        def area(self):
        that raises an Exception with the message area() is not implemented
        def integer_validator(self, name, value):
        validates value"""


class BaseGeometry:
    """ Class BaseGeometry """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0')