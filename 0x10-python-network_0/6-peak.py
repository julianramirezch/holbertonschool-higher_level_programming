#!/usr/bin/python3
"""  finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ function that finds a peak in a list of unsorted integers """
    lenght = len(list_of_integers) - 1
    if lenght <= 0:
        return None

    middle = int(lenght / 2)
    right = list_of_integers[middle]
    left = list_of_integers[middle - 1]

    if (middle == lenght or right >= list_of_integers[middle + 1])\
            and (middle == 0 or right >= left):
        return right
    elif middle != lenght and list_of_integers[middle + 1] > right:
        idx = middle + 1
        return find_peak(list_of_integers[idx:])
    return find_peak(list_of_integers[:middle])
