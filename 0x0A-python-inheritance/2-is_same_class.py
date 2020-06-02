#!/usr/bin/python3
""" Module: 2-is_same_class - True if object is exactly an instance of the class"""


def is_same_class(obj, a_class):
    if type(obj) == a_class:
        return True
    else:
        return False
