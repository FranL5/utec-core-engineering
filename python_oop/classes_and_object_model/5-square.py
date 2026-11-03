#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.__size = size

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size)
