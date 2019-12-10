#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    l_num = number % -10
elif number >= 0:
    l_num = number % 10
if l_num > 5:
    print("Last digit of {:d} is {:d} and is \
greater than 5".format(number, l_num))
if l_num < 6 and l_num is not 0:
    print("Last digit of {:d} is {:d} \
and is less than 6 and not 0".format(number, l_num))
if l_num is 0:
    print("Last digit of {:d} is {:d} \
and is 0".format(number, l_num))