#!/usr/bin/python3

"""Defines a class named square"""

class Square:
    """Class square with attribute size"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:                
            raise ValueError("size must be>= 0")
        self.__size = size
