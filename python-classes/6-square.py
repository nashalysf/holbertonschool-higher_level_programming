#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Square:
    """class that defines a square
    Attributes: 
        size: size of square
    """

    def __init__(self, size=0, position=(0, 0)):
        """init method for square
        Args:
            size private instance size
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """property getter / checks property
        Returns:
            size of square
        """
        return self.__size

    @property
    def position(self):
        "retrieves position"
        return self.__position

    @size.setter
    def size(self, value):
        """size method that sets value as attribute
            Args:
                value: size to set attribute to
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """sets position value"""
        if value is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position - value

    def area(self):
        """Calculate area of square
            Returns:
                square ** 2
        """
        return self.__size ** 2

    def my_print(self):
        """Prints stdout the square size in #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(end=" ")
                for x in range(self.size):
                    print("#", end="")
                print()
