#!/usr/bin/python3
"""A rectangle class.
TODO:
    here i am just going to create a rectangle class.
    For this class, i'll create some attributes and methods.
    Then i'll customize my error messages.
    That is  pretty much i'll be doing.
    Calculate the area and perimeter.

Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise raise a TypeError exception with the message width must be an integer
if width is less than 0, raise a ValueError exception with the message width must be >= 0
Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise raise a TypeError exception with the message height must be an integer
if height is less than 0, raise a ValueError exception with the message height must be >= 0
Instantiation with optional width and height: def __init__(self, width=0, height=0):
 """
class Rectangle:
    """ here i'll instantiate some attributes """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        """
        args:
            width (integer)
            height (integer)
        """
    @property
    def width(self):
        """
        Returns:
            width (integer)
        """
        return self.__width
    @property
    def height(self):
        """
        Returns:
            height (integer)
        """
        return self.__height
    @width.setter
    def width(self, value):
        """
        Args:
            value (integer)
         """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """"
        Args:
            height (integer)

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculate the area of a rectangle
        Returns:
            area (integer)
        """
        return self.__height * self.width

    def perimeter(self):
        """ calculate the perimeter of a rectangle
        Returns:
            perimeter (integer)
         """
        return((2 * self.width) + (2 * self.height))
