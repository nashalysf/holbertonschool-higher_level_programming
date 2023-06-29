#!/usr/bin/python3
"""Module with class Rectangle"""
import json
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of Square"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))
