#!/usr/bin/python3
""" Module: 7-rectangle - superClass BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle """
    def __init__(self, width, height):
        """
            Instantiation with width and height
        """
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
