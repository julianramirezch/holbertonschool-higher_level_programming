#!/usr/bin/python3
""" class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """ Class define a Square
            Args:
                size (int): Size of Square.

            Returns:
                None.

            Raises:
                TypeError: If size is not an integer
                ValueError: If `size` is minor to 0.
        """
    def __init__(self, size=0, area=0):
        self.size = size
        self.__area = area

    @property
    def size(self):
        """ Getter of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Set value of size """
        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """ Return current square area """
        return (self.__size ** 2)
