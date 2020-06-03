#!/usr/bin/python3
""" Module: 1-my_list -  inherits from list , prints sorted list"""


class MyList(list):
    """Class define MyList"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
