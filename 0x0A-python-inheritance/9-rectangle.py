#!/usr/bin/python3
"""Rectangle inherit from BaseGeometry defined."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle using BaseGeometry rep."""

    def __init__(self, width, height):
        """Runs new Rectangle.

        Args:
            width (int): width of new Rectangle.
            height (int): height of new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area of the rectangle returned."""
        return self.__width * self.__height

    def __str__(self):
        """Print() and str() rep of Rectangle Returned."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
