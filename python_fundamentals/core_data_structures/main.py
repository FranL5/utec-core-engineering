#!/usr/bin/env python3

element_at = __import__('element_at').element_at

my_list = ["a", "b", "c", "d", "e"] 
print(element_at(my_list, 2)) 
print(element_at(my_list, -2)) 
print(element_at(my_list, 12)) 
print(element_at(my_list, 0))
