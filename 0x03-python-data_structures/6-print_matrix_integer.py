#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print('')
    else:
        for x in matrix:
            col = 0
            for y in x:
                if col == (len(x) - 1):
                    print('{:d}'.format(y), end='')
                else:
                    print('{:d}'.format(y), end=' ')
                col += 1
            print('')
