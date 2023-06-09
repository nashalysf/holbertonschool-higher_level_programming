#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python OOP: classes
"""


class Square:
    """class that defines a square
    Attributes:
        size: size of square
    """

    def __init__(self, size=0):
        """init method for square
        Args:
            size private instance size
        Raises:
            TypeError: exception if size is not an int
            ValueError: exception if size < 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
