#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" 
Python TDD 
"""


def add_integer(a, b=98):
    """
    Function: add 2 ints
    """
    if type(a) is not int:
        raise TypeError("a must be an integer or b must be an integer")
    if type(b) is not int:
        raise TypeError("a must be an integer or b must be an integer")
    a_int = int(a)
    b_int = int(b)

    return (a + b)
