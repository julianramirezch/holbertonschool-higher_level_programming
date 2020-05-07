#!/usr/bin/python3
def number_keys(a_dictionary):
    cont = 0
    for i in dict(a_dictionary):
        cont += 1
    return cont
