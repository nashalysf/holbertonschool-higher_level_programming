#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        end = ""
        for element in row:
            print("{:s}{:d}".format(end, element), end="")
            end = " "
        print()
