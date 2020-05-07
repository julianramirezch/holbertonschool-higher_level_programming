#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        matrix_row = []
        for y in x:
            matrix_row.append(y**2)
        new_matrix.append(matrix_row)

    return new_matrix
