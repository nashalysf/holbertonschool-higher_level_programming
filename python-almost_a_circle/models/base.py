#!/usr/bin/python3
"""Module with class Base"""
import json


class Base:
    """Base super class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects