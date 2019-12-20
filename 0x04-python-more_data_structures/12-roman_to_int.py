#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is str:  # checks if input a string
# rests to 0 when program compares
# multiple roman numerals, like IX
        num = 0
        holder = 0
        prev = 10000
        for c in roman_string:
# checks dictionary to see if input matches any of the contents
            if c in dic:
# now holder is set to value of input, like if user typed "X" holder would = 10
                holder = dic[c]
            else:
                return (0)
            if holder <= prev:
                num += holder  # num is same value as holder
# prev is same value as holder,
# this is incase user types in multiple roman numerals
                prev = holder
            else:
                num += holder - prev * 2
        return num
    return 0  # If the roman_string is not a string or None, return 0
