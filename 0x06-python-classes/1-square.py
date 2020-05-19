#!/usr/bin/python3
""" class Square that defines a square by: (based on 0-square.py)
    Private instance attribute: size
    Instantiation with size (no type/value verification)
"""


class Square:
    """ Class define a Square"""
    def __init__(self, size=0):
        self.__size = size
