#!/usr/bin/python3
i = 0
for n in range(122, 96, -1):
    print("{0}".format(chr(n - i)), end="")
    if i == 0:
        i = 32
    else:
        i = 0
