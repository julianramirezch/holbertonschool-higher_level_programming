#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    for x in matrix:
        col = 0
        if rows == 1 and enumerate(matrix) == 0:
            print('')
        else:
            for y in x:
                if col == (len(x) - 1):
                    print('{}'.format(y), end='')
                else:
                    print('{}'.format(y), end=' ')
                col += 1
            print('')
