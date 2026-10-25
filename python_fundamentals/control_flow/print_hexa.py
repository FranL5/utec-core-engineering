#!/usr/bin/env python3
print(
    "\n".join(
        "{} = {}".format(number, hex(number))
        for number in range(99)
     )
)
