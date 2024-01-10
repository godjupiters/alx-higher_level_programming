#!/usr/bin/python3
"""Rectangle subclass Defined."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Rep square."""

    def __init__(self, size):
        """Runs new square.

        Args:
            size (int): size of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
