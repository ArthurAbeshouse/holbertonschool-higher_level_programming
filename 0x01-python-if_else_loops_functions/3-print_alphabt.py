#!/usr/bin/python3
for n in range(ord('a'), ord('z') + 1):
    if n != ord('q') and n != ord('e'):
        print("{}".format(chr(n)), end="")
