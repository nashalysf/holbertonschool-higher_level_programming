#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python TDD
"""


def say_my_name(first_name, last_name=""):
    """Functon that prints name

    Args:
        first_name (str): first name
        last_name (str): last name
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    else:
        print(f"My name is {first_name} {last_name}")
