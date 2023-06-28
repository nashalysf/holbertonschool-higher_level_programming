#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python: Object Inheritance
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):

    """
    square subclass inheriting from rectangle

    """

    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def __str__(self):
        """string that prints width and height
        """
        return ('[Square]' + str(self.__size) + '/' + str(self.__size))

    def area(self):
        """returns area of Square
        """
        return (self.__size ** 2)
