#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        fct = fct(*args)
    except Exception as CatchMessage:
        print('Exception: {}'.format(CatchMessage), file=stderr)
        return None
    return fct
