#!/usr/bin/python3
""" prevents the user from dynamically creating new instance attributes"""


class LockedClass:
    """Locked class"""
    __slots__ = ['first_name']
