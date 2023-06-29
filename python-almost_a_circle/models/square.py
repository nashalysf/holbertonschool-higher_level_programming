#!/usr/bin/python3
"""Module with class Rectangle"""
import json
from models.base import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the size of the square"""
        return self.width

    def __str__(self):
        """Return a string representation of Square"""
        return ("[Square] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width))
