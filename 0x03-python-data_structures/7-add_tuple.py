#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenght_a = len(tuple_a)
    lenght_b = len(tuple_b)

    if lenght_a < 2:
        tuple_a = tuple_a + (0, 0)
    if lenght_b < 2:
        tuple_b = tuple_b + (0, 0)

    x = tuple_a[0] + tuple_b[0]
    y = tuple_a[1] + tuple_b[1]
    return x, y
