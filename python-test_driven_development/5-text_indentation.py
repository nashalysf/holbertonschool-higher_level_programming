#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python TDD
"""


def text_indentation(text):
    """generates string

    Args:
        text (str): _description_
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    string = ""
    for char in text:
        string += char
        if char in ["?", ".", ":"]:
            string += "\n\n"
    print(string, end='')
