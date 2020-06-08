#!/usr/bin/python3
""" Module: Rectangle """

from models.base import Base


class Rectangle(Base):
    """ Rectangle subclass """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Return Rectangle Area """
        return self.__width * self.__height

    def display(self):
        """ Print Rectangle with '#' """
        for row in range(self.__y):
            print('')
        for character in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """ String representation """
        x_ = self.__x
        y_ = self.__y
        w_ = self.__width
        h_ = self.__height
        id_ = self.id
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(id_, x_, y_, w_, h_))

    def update(self, *args, **kwargs):
        """ Assign argument to each attribute """
        index = 1
        if len(args):
            for arg in args:
                if index == 1:
                    self.id = arg
                if index == 2:
                    self.width = arg
                if index == 3:
                    self.height = arg
                if index == 4:
                    self.x = arg
                if index == 5:
                    self.y = arg
                index += 1
        if len(kwargs):
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs.get(key)
                if key == 'width':
                    self.width = kwargs.get(key)
                if key == 'height':
                    self.height = kwargs.get(key)
                if key == 'x':
                    self.x = kwargs.get(key)
                if key == 'y':
                    self.y = kwargs.get(key)

    def to_dictionary(self):
        """ dictionary representation of a Rectangle """
        dicti = {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
        }
        return dicti
