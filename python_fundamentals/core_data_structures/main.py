#!/usr/bin/env python3

replace_in_list = __import__('replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
print(f"lista antes: {my_list}")
print(f"lista despues 1: {replace_in_list(my_list, 3, 99)}")
print(f"lista despues 2: {replace_in_list(my_list, 15, 99)}")
print(f"lista despues 3: {replace_in_list(my_list, 0, 9)}")
