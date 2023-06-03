#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = len(sys.argv) - 1

    if i == 0:
        print(f"{i} arguments.")
    elif i == 1:
        print(f"{i} argument:")
    else:
        print(f"{i} arguments:")

    if i >= 1:
        i = 0
        for arg in sys.argv:
            if i != 0:
                print(f"{i}: {arg}")
            i += 1
