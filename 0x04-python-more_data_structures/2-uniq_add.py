#!/usr/bin/python3


def add_list(copy_list):
    res = 0
    for i in copy_list:
        res += int(i)
    return res


def uniq_add(my_list=[]):
    new_list = []
    copy_list = sorted(my_list)
    for i in range(len(copy_list)):
        if copy_list[i] != copy_list[i - 1]:
            new_list.append(copy_list[i])

    return add_list(new_list)
