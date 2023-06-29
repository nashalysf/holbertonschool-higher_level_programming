#!/usr/bin/python3
"""Module with class Rectangle"""
import json
from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        if value is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            ValueError("width must be > 0")

    @property
    def height(self):
        """Getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if value is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            ValueError("height must be > 0")

    @property
    def x(self):
        """Getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        if value is not int:
            raise TypeError("x must be an integer")
        if value <= 0:
            ValueError("x must be >= 0")

    @property
    def y(self):
        """Getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        if value is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            ValueError("y must be >= 0")
