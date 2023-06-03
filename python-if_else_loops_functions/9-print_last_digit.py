#!/usr/bin/python3
def print_last_digit(number):
    digit = abs(number) % 10
    print("{:2d}".format(digit))
    return digit
