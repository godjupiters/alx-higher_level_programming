#!/usr/bin/python3

"""Define a class"""


class Square:
    """Represents a square with a given size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with the given size and position.

        Args:
            size (int, optional): The initial size of the square.

        Raises:
            TypeError: If size is not an integer or position is not a valid.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get current size of square."""
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
        """Gets the current position of the square.

        Returns:
            tuple: A tuple of (x, y) coordinates representing the square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square with # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for z in range(0, self.__position[1])]
        for z in range(0, self.__size):
            [print(" ", end="") for a in range(0, self.__position[0])]
            [print("#", end="") for b in range(0, self.__size)]
            print("")
