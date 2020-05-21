#!/usr/bin/python3
""" Module: 2-matrix_divided - divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix."""
    matrix_error = 'matrix must be a matrix (list of lists) of integers/floats'
    row_error = 'Each row of the matrix must have the same size'
    div_error = 'div must be a number'
    div_list = []

    if type(matrix) is not list:
        raise TypeError(matrix_error)
    if type(div) is not int and float:
        raise TypeError(div_error)
    if div == 0:
        raise ZeroDivisionError('division by zero')

    for items in matrix:
        if type(items) is not list:
            raise TypeError(matrix_error)
        row = []
        for num in items:
            if type(num) is not int and float:
                raise TypeError(matrix_error)
            row.append(round((num / div), 2))
        div_list.append(row)

    return div_list
