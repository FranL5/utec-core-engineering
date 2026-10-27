#!/usr/bin/env python3
"""Convierte un string a un archivo de texto UTF-8."""


def write_file(filename="", text=""):
    """Envía texto a un archivo y retorna el numero de caracteres escritos."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
