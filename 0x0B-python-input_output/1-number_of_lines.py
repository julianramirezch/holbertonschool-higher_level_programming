#!/usr/bin/python3
""" Module: 1-number_of_lines """


def number_of_lines(filename=""):
    """function that returns the number of lines of a text file"""
    cont = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            cont += 1
    return cont
