#!/usr/bin/python3
def uppercase(str):
    for c in str:
        chr = ord(c)
        if (chr >= 97) and (chr <= 122):
            chr -= 32
            print("{:c}".format(chr), end='')
    print()
