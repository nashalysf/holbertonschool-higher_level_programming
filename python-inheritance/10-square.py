#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python: Object Inheritance
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """
    square subclass inheriting from rectangle

    """

    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator('size', size)
        self.__size = size
