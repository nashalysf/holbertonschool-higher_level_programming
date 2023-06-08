#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    new_d = a_dictionary.copy()
    if key in new_d:
        del new_d[key]
    return (new_d)
