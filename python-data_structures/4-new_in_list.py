#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if 0 > idx or idx >= len(my_list):
        return my_list[:]
    new_l = my_list[:]
    new_l[idx] = element
    return (new_l)
