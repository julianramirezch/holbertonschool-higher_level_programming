#!/usr/bin/python3


def roman_to_int(roman_string):
    r_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    values = []
    num = 0

    if type(roman_string) is str:
        for i in roman_string:
            values.append(r_num.get(i))

        index = len(values)
        for j in range(index):
            if j == index - 1:
                num += values[j]
            elif values[j] < values[j + 1]:
                num -= values[j]
            else:
                num += values[j]

    return num
