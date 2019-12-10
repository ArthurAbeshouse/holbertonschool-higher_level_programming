#!/usr/bin/python3
for num in range(0, 100):
    if num in range(0, 99):
        print("{}, ".format(format(num, '02d')), end='')
    else:
        print(num)
