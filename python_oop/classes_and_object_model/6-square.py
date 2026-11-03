#!/usr/bin/env python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.__position = (0, 0)
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or len(value) != 2 or
                any(type(n) is not int or n <= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integer")

        self.__position = value

    def my_print(self):
        if self.size == 0:
            print()
            return

        for i in range(self.position[1]):
            print()

        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        if self.size == 0:
            return ""

        result = "\n" * self.position[1]

        for i in range(self.size):
            result += " " * self.position[0] + "#" * self.size

            if i < self.size - 1:
                result += "\n"

        return result