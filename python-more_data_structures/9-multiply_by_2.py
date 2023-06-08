#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_d = a_dictionary.copy()
    new_d = ([[(x * 2) for x in key] for key in new_d])
    return (new_d)