#!/usr/bin/python3
""" Module: 4-rectangle.py - defines a rectangle:(based on 3-rectangle.py)"""


class Rectangle:
    """Class define a Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.__height and self.__width is 0:
            return 0
        else:
            return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        rec = ''
        if self.__width or self.__height is not 0:
            for i in range(self.__height):
                if i < self.__height - 1:
                    rec += ('#' * self.__width) + '\n'
                else:
                    rec += ('#' * self.__width)
            return rec
        else:
            return rec

    def __repr__(self):
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)
