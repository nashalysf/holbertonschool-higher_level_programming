#!/usr/bin/python3
def uppercase(str):
    for c in str:
        chr = ord(c)
        if (chr >= 65) and (chr <= 90):
            print("{:c}".format(chr), end='')
    print()
