#!/usr/bin/python3
# how to import fun() from other files
# how to use fun() from other file
# how to create a module
# how to prevent code in your script from being executed when imported
# how to use comman dline args with your python programs

if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
