#!/usr/bin/python3
"""Module: 3-say_my_name - prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """Function that prints My name is <first name> <last name>"""
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    first = first_name
    last = last_name
    print('My name is {} {}'.format(first, last))
