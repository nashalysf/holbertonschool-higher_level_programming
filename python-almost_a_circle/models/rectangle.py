#!/usr/bin/python3
"""Module with class Rectangle"""
import json
from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
