#!/usr/bin/python3
"""  finds a peak in a list of unsorted integers """


# def find_peak(list_of_integers):
#     """ function that finds a peak in a list of unsorted integers """
#     lenght = len(list_of_integers)
#     if lenght != 0:
#         idx = find_peak_2(list_of_integers, 0, lenght, lenght)
#         # print('idx {}'.format(idx))
#         return list_of_integers[idx]


# def find_peak_2(list_n, low, high, lenght):
#     middle = int(low + (high - low)/2)
#     # print('middle {} lenght {}'.format(middle, lenght))

#     if (middle == 0 or list_n[middle - 1] <= list_n[middle]) and\
#             (middle == lenght - 1 or list_n[middle + 1] <= list_n[middle]):
#         return middle
#     if middle > 0 and list_n[middle - 1] > list_n[middle]:
#         return find_peak_2(list_n, low, middle, lenght)
#     else:
#         return find_peak_2(list_n, middle, high, lenght)

def find_peak(list_of_integers):
    """ function that finds a peak in a list of unsorted integers """
    if len(list_of_integers) != 0:
        list_of_integers.sort()
        return (list_of_integers[-1])
