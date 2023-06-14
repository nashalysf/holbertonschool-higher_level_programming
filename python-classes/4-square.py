#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Square:
    """class that defines a square
    Attributes: 
        size: size of square
    """

    def __init__(self, size=0):
        """init method for square
        Args:
            size private instance size
        """
        self.__size = size

    @property
    def size(self, value):
        """size method that sets attribute to value
            Args:
            value: size to set attribute to
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate area of square
            Returns:
            square ** 2
        """
        return self.__size ** 2
