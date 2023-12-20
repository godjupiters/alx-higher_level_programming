#!/usr/bin/python3

"""Define class"""


class Square:
    """ Representing Function"""

    def __init__(self, size=0):
        """Initialization of function

        Args:
            size (int): variable holding size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
