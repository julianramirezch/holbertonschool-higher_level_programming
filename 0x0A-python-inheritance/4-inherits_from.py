#!/usr/bin/python3
""" Module: 4-inherits_from - returns True if the object is an instance of"""


def inherits_from(obj, a_class):
    if issubclass(type(obj), a_class) is True:
        if type(obj) != a_class:
            return True
    else:
        return False
