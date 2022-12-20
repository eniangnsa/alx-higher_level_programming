#!/usr/bin/python3
""""
This is a class that returns the area of a square
"""
class Square:
    """
        Atrributes:
            __init__ (function): assign and validate attributes
            area (function): calculate area of square
    """
    def __init__(self, size=0):
        """
        Args:
            self (Square): object
            size (int): size of square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        Args:
            self (Square): instance of class
        Return:
            area (int)
        """
        return (self.__size * self.__size)
