#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    l_num = number % -10
else:
    l_num = number % 10
print("The last digit of", '{:d}'.format(number), "is", '{:d}'.format(l_num), end="")

if l_num > 5:
    print(" and is greater than 5")
elif l_num == 0:
    print(" and is 0")
elif l_num < 6:
    print(" and is less than 6 and not 0")