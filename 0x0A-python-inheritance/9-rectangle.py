#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" Module: 7-rectangle - superClass BaseGeometry"""


class Rectangle(BaseGeometry):
    """ Class Rectangle """
    def __init__(self, width, height):
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))