#!/usr/bin/python3
"""Rectangle inherits from BaseGeometry Defined."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle using Base_Geometry Rep."""

    def __init__(self, width, height):
        """Runs new Rectangle.

        Args:
            width (int): width of new Rectangle.
            height (int): height of new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
