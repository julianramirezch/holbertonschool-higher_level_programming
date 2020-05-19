#!/usr/bin/python3
""" class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """ Class define a Square"""

    def __init__(self, size=0, area=0):
        """
            Args:
                size (int): Size of Square.
                area (int): Area of Square

            Returns:
                None.

            Raises:
                TypeError: If size is not an integer
                ValueError: If `size` is minor to 0.
        """
        self.__size = size
        self.__area = area
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """
            Args:
                self : Square.

            Return:
                Current square area.
        """
        return (self.__size ** 2)
