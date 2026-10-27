#!/usr/bin/env python3
"""Añade un string a un archivo de texto UTF-8."""


def append_write(filename="", text=""):
    """Añade texto a un archivo y retorna el numero de caracteres añadidos."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
    