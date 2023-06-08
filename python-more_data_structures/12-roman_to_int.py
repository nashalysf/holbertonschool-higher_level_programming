#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return (0)

    result = 0
    roman_data = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_list = list(roman_string.upper())

    for value in roman_list:
        result += roman_data[value]
