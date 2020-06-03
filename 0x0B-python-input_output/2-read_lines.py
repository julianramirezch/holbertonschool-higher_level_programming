#!/usr/bin/python3
""" Module: 2-read_lines """


def read_lines(filename, nb_lines=0):
    """ function that reads n lines of a text file (UTF8) and prints it
        to stdout"""
    with open(filename, mode='r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read())
        else:
            for i in range(nb_lines):
                print(f.readline(), end='')
