#!/usr/bin/python3
""" Module: 9-rectangle - superClass Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size):
        super().__init__(size, size)
        super().integer_validator('size', size)
        self.__size = size
