#!/usr/bin/python3
class Square:
    """A class with a 'size' attribute"""
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
