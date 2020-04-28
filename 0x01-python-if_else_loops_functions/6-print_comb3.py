#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if y != x and y != 0 and x <= 8:
            if x < y and x != 8:
                print("{}{}, ".format(x, y), end='')
            if x < y and x == 8:
                print("{}{}".format(x, y))
