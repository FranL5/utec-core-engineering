#!/usr/bin/env python3
"""Define la clase Square."""


class Square:
    """Representa un cuadrado."""

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa el cuadrado."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Obtiene el tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Valida y establece el tamaño del cuadrado."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Obtiene la posición del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Valida y establece la posición del cuadrado."""
        if (type(value) is not tuple or len(value) != 2 or
                any(type(n) is not int or n < 0 for n in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

    def area(self):
        """Calcula y devuelve el área del cuadrado."""
        return self.__size ** 2

    def my_print(self):
        """Imprime el cuadrado utilizando el carácter #."""
        print(self)

    def __str__(self):
        """Devuelve la representación del cuadrado como una cadena."""
        if self.__size == 0:
            return ""

        spaces = " " * self.__position[0]
        row = spaces + "#" * self.__size

        return "\n" * self.__position[1] + "\n".join(
            [row] * self.__size
        )
