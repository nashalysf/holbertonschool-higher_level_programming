#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python OOP: more classes
"""


class Rectangle:
    """Rectangle class
    Attributes:
        width: width of rectangle
        height: height of rectangle
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

    def area(self):
        """"Returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """"Returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            string = ""
            for i in range(self.__height):
                if i == self.__height - 1:
                    string += self.__width * '#'
                else:
                    string += self.__width * '#' + '\n'
            return string
