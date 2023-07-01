#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python TDD
"""


def matrix_divided(matrix, div):
    """Function to divide a matrix
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
        return matrix
    elif div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix
    else:
        raise TypeError(
            "matrix must be a matrix (list of lists)" + " of integers/floats")
        return matrix
    new_matrix[i][j] = round(matrix[i][j] / div, 2)

    return new_matrix
