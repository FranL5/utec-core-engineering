#!/usr/bin/env python3
"""Define la clase Square."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0):
        """Inicializa el cuadrado."""
        self.__size = size

    def area(self):
        """Devuelve el área del cuadrado."""
        return self.__size ** 2
