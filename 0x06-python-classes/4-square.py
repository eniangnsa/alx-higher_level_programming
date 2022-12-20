#!/usr/bin/python3
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
        self.__size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Args:
            self (Square): instance of class
        Return:
            area (int)
        """
        return (self.__size * self.__size)
