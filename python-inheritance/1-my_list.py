#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Python: Object Inheritance
"""

class MyList(list):
    """
    Inherits from list
    """

    
    def print_sorted(self):
        self.sort()
        print(self)
