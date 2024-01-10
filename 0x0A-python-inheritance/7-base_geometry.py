#!/usr/bin/python3
"""Base geometry class defined."""


class BaseGeometry:
    """Base geometry rep."""

    def area(self):
        """Pending."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Parameter as integer to validate.

        Args:
            name (str): name of parameter.
            value (int): parameter to validate.
        Raises:
            TypeError: value is not int.
            ValueError: value <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
