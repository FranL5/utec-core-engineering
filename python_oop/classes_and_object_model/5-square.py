#!/usr/bin/env python3
"""Define la clase Square."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa el cuadrado."""
        self.__size = size

    def my_print(self):
        """Imprime el cuadrado utilizando el carácter #."""
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size)
