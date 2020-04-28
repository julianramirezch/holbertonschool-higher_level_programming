#!/usr/bin/python3
def print_last_digit(number):
    j = abs(number)
    print("{}".format(j % 10), end='')
    return j % 10
