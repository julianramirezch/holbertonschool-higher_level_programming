#!/usr/bin/python3
def multiple_returns(sentence):
    lenght = len(sentence)
    first = None
    if sentence == '':
        return lenght, first
    else:
        first = sentence[0]
        return lenght, first
