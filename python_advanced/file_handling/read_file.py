#!/usr/bin/env python3
"""Lee e imprime el contenido de un archivo de texto UFT-8."""


def read_file(filename=""):
    """Lee un archivo e imprime su contenido como stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

