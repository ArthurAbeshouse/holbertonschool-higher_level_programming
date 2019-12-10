#!/usr/bin/python3
for n in range(ord('a'), ord('z') + 1):
    if n in [101,113]:
        continue
    print("{}".format(chr(n)), end='')
