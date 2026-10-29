#!/usr/bin/env python3
"""Módulo que define la clase Square con un tamaño privado."""


class Square():
    """Representa un cuadrado geométrico."""

    def __init__(self, size):
        """Inicializa una nueva instancia de Square.
        Args:
            size: Tamaño del lado del cuadrado.
        """
        self.__size = size