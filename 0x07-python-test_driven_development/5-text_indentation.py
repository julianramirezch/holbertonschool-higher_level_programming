#!/usr/bin/python3
""" Module: 5-text_indentation - prints a text with 2 new lines after: .,?,:"""


def text_indentation(text):
    """function that prints a text with 2 new lines after: ., ? and :"""
    if type(text) is not str:
        raise TypeError('text must be a string')
    new_text = text
    new_text = new_text.replace('. ', '.\n\n')
    new_text = new_text.replace('? ', '?\n\n')
    new_text = new_text.replace(': ', ':\n\n')
    print(new_text, end='')
