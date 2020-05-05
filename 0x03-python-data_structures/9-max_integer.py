#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        lenght = len(my_list)
        sort_list = sorted(my_list)
        return sort_list[lenght - 1]
