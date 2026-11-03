#!/usr/bin/env python3
"""Módulo que define la clase BaseGeometry."""


class BaseGeometry:
    """Clase base para figuras geométricas."""

    def area(self):
        """Lanza una excepción indicando que el área no está implementada."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que un valor sea un entero estrictamente positivo (> 0).

        Args:
            name (str): nombre del parámetro o variable a validar.
            value (int): valor a comprobar.

        Raises:
            TypeError: si value no es un entero.
            ValueError: si value es menor o igual a 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
