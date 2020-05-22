#!/usr/bin/python3
""" Module: 0-add_integer - add two integers """


def add_integer(a, b=98):
    """Function that adds 2 integers and check a,b are int or float
        Args:
            a (int): Integer
            b (int): Integer
        Returns:
            int(a) + int(b)
    """
    if a is not None:
        if type(a) not in [float, int]:
            raise TypeError('a must be an integer')
        elif type(b) not in [float, int]:
            raise TypeError('b must be an integer')
        else:
            return int(a) + int(b)
    else:
        if a is None:
            raise TypeError('a must be an integer')
