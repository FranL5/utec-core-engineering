#!/usr/bin/env python3

def common_elements(set_1, set_2):
    set_3 = set()
    for item in set_1:
        if item in set_2:
            set_3.add(item)
    return set_3
