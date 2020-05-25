#!/usr/bin/python3
""" Module: 8-rectangle.py - defines a rectangle:(based on 7-rectangle.py)"""


class Rectangle:
    """Class define a Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

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
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        rec = ''
        symbol = str(self.print_symbol)

        if self.__width == 0 or self.__height == 0:
            return rec

        for i in range(self.__height):
            if i < self.__height - 1:
                rec += (symbol * self.__width) + '\n'
            else:
                rec += (symbol * self.__width)

        return rec

    def __repr__(self):
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print('Bye rectangle...')
