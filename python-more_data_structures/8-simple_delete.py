#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    new_d = a_dictionary.copy()
    if key in new_d:
        new_d.pop(key)
    return (new_d)
