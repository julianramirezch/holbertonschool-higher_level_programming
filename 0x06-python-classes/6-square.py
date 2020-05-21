#!/usr/bin/python3
""" class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """ Class define a Square
                Args:
                size (int): Size of Square.
                area (int): Area of Square
                position (int): Position of square
            Returns:
                None.
            Raises:
                TypeError: If size is not an integer
                        If position is not a tuple
                ValueError: If `size` is minor to 0.
    """

    def __init__(self, size=0, position=(0, 0), area=0):
        """Instantiation"""
        self.size = size
        self.position = position
        self.__area = area

    @property
    def size(self):
        """ Getter of size"""
        return self.__size

    @property
    def position(self):
        """ Getter of position"""
        return self.__position

    @size.setter
    def size(self, value):
        """ Set value of size """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """ Set value of position """
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif len(value) is not 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """ Return current square area """
        return (self.__size ** 2)

    def my_print(self):
        """ Prints in stdout the square with the character # """
        size = self.__size
        x, y = self.__position

        if size == 0:
            print('')
        else:
            for i in range(y):
                print('')
            for j in range(size):
                print(' ' * x + '#' * size)
