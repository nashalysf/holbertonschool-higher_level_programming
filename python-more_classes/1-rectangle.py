#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python OOP: more classes
"""


class Rectangle:
    """Rectangle class
    Attributes:
        width: width of rectangle
    """

    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (int)
            height (int)
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """GETTER: retrieves width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """SETTER: sets width of rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """GETTER: retrieves height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """SETTER: sets height of rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
