#!/usr/bin/env python3


def safe_print_integer(value):    
    nb_print = 0
    for i in range(x):
        try:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                nb_print += 1
        except IndexError:
            break
    print()
    return nb_print
