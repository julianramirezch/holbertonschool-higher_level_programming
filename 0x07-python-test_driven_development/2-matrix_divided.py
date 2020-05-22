#!/usr/bin/python3
""" Module: 2-matrix_divided - divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix."""

    matrix_error = 'matrix must be a matrix (list of lists) of integers/floats'
    row_error = 'Each row of the matrix must have the same size'
    div_error = 'div must be a number'
    div_list = []

    if matrix == []:
        raise IndexError(matrix_error)
    else:
        size = len(matrix[0])

        if type(matrix) is not list:
            raise TypeError(matrix_error)
        if type(div) not in [float, int] or div is None:
            raise TypeError(div_error)
        if div == 0:
            raise ZeroDivisionError('division by zero')

        for items in matrix:
            if type(items) is not list:
                raise TypeError(matrix_error)
            row = []
            row_size = 0
            for num in items:
                if type(num) not in [float, int]:
                    raise TypeError(matrix_error)
                row.append(round((num / div), 2))
            row_size = len(row)
            if size != row_size:
                raise TypeError(row_error)
            div_list.append(row)

        return div_list
