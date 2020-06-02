#!/usr/bin/python3
""" Module: 6-base_geometry - Class BaseGeometry"""


class BaseGeometry:
    """ Class BaseGeometry """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Validate if value is integer and more than 0"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0')
