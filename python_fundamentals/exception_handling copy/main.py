#!/usr/bin/env python3
safe_print_list = __import__('safe_print_list').safe_print_list

my_list = [2, 1, 3, 4, 5]

nb_print = safe_print_list(my_list, 5)
print(f"elements: {nb_print}")
