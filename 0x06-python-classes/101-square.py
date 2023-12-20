#!/usr/bin/python3

"""Define Class"""


class Square:
    """Represents a square with a given size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with the given size and position.

        Args:
            size (int, optional): The initial size of the square's side.
            position (tuple, optional): The initial position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(data, int) for data in value) or
                not all(data >= 0 for data in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """
        Prints a visual representation of the square.
        """
        if self.__size == 0:
            print("")
            return

        [print("") for z in range(0, self.__position[1])]
        for z in range(0, self.__size):
            [print(" ", end="") for a in range(0, self.__position[0])]
            [print("#", end="") for b in range(0, self.__size)]
            print("")

    def __str__(self):
        """
        Returns a string representation of the square, similar to my_print.
        """
        if self.__size != 0:
            [print("") for z in range(0, self.__position[1])]
        for z in range(0, self.__size):
            [print(" ", end="") for a in range(0, self.__position[0])]
            [print("#", end="") for b in range(0, self.__size)]
            if z != self.__size - 1:
                print("")
        return ("")
