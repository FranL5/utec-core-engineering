#!/usr/bin/env python3
"""Define la clase Rectangle."""


class Rectangle:
    """Representa un rectángulo."""

    def __init__(self, width=0, height=0):
        """Inicializa el rectángulo."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Obtiene el ancho del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Valida y establece el ancho del rectángulo."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Obtiene la altura del rectángulo."""
        return self.__height

    @height.setter
    def height(self, value):
        """Valida y establece la altura del rectángulo."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcula y devuelve el área del rectángulo."""
        return self.__width * self.__height

    def perimeter(self):
        """Calcula y devuelve el perímetro del rectángulo."""
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)
