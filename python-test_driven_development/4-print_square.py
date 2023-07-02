#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python TDD
"""


def print_square(size):
    """Functon that prints square in #

    Args:
        size (int): length of square
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')
