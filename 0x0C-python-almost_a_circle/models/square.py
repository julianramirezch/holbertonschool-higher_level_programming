#!/usr/bin/python3
""" Module: Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """ in Square width is equal to height """
        self.width = value
        self.height = value

    def __str__(self):
        """ String representation """
        x_ = self.x
        y_ = self.y
        s_ = self.width
        id_ = self.id
        return ("[Square] ({}) {}/{} - {}".format(id_, x_, y_, s_))

    def update(self, *args, **kwargs):
        """ Assign argument to each attribute """
        index = 1
        if len(args):
            for arg in args:
                if index == 1:
                    self.id = arg
                if index == 2:
                    self.width = arg
                    self.height = arg
                if index == 3:
                    self.x = arg
                if index == 4:
                    self.y = arg
                index += 1
        if len(kwargs):
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs.get(key)
                if key == 'size':
                    self.width = kwargs.get(key)
                    self.height = kwargs.get(key)
                if key == 'x':
                    self.x = kwargs.get(key)
                if key == 'y':
                    self.y = kwargs.get(key)

    def to_dictionary(self):
        """ dictionary representation of a Square """
        dicti = {
            'id': self.id,
            'x': self.x,
            'size': self.width,
            'y': self.y
        }
        return dicti
