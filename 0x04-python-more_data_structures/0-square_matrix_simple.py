#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        row = []
        for y in x:
            row.append(y**2)
        new_matrix.append(row)

    return new_matrix
