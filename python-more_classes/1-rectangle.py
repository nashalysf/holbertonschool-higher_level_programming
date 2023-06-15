#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python OOP: more classes
"""


class Rectangle:
    """Empty Rectangle class
    Attributes:
        width: width of rectangle
    """

    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (_type_): _description_
        """

        self._width = width
        self._height = height

    @property
    def width(self):
        """GETTER: retrieves width of rectangle"""
        return self._width

    @property
    def height(self):
        """GETTER: retrieves height of rectangle"""
        return self._height

    @width.setter
    def width(self, value):
        """SETTER: sets width of rectangle"""
        if value is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value

    @height.setter
    def height(self, value):
        """SETTER: sets height of rectangle"""
        if value is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value
