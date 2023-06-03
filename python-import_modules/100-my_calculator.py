#!/usr/bin/python3

if __name__ == "__main__":
    # ask the user to enter two values and store them in variables
    num1, op, num2 = input().split()

    # convert user input(str) into int
    num1 = int(num1)
    num2 = int(num2)

    # add
    if op == "+":
        sum = num1 + num2
        print(f"{num1} + {num2} = {sum}")
    # subtract
    elif op == "-":
        sub = num1 - num2
        print(f"{num1} - {num2} = {sub}")
    # mutiply
    elif op == "*":
        mul = num1 * num2
        print(f"{num1} * {num2} = {mul}")
    # divide
    elif op == "/":
        div = num1 / num2
        print(f"{num1} / {num2} = {div}")
    # reminder
    elif op == "%":
        mod = num1 % num2
        print(f"{num1} % {num2} = {mod}")
    # none
    else:
        print(f"Please enter a valid operator: +  -  *  /  %")
