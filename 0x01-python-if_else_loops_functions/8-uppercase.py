#!/usr/bin/python3
def uppercase(str):
    for n in str:
        if ord(n) in range(ord('a'), ord('z') + 1):
            n = chr(ord(n) - 32)
        print("{}".format(n), end="")
    print("")
