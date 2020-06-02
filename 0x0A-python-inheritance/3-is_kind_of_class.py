#!/usr/bin/python3
"""Module: 3-is_kind_of_class - returns True if the object is an instance of"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
