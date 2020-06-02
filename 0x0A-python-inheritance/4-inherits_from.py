#!/usr/bin/python3
""" Module: 4-inherits_from - returns True if the object is an instance of"""


def inherits_from(obj, a_class):
    """ returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class"""
    if issubclass(type(obj), a_class):
        if type(obj) is not a_class:
            return True
    else:
        return False
