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
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (int)
            height (int)
        """

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
                    string += self.__width * str(self.print_symbol)
                else:
                    string += self.__width * str(self.print_symbol) + '\n'
            return string

    def __repr__(self):
        """Returns a string representation printable"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """destroctor"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """params are instances of rectangle class"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_2.area() >= rect_1.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns new rectangle instance"""
        if size is not int:
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        __height = size
        __width = size
        return cls(__height, __width)
