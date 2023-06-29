#!/usr/bin/python3
"""Module with class Rectangle"""
import json
from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Base

        Attributes:
        width: private int attribute of rectangle
        height: private int attribute of rectangle
        x: private int attribute of rectangle
        y: private int attribute of rectangle
        id: private int attribute inherited from Base
        """

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
        """Setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Display the rectangle"""
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return ("[Rectangle] ({}) <{}>/<{}> - <{}>/<{}>".format(self.__id, self.__x, self.__y, self.__width, self.__height))
