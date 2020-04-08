#!/usr/bin/python3
"""Technical interview preparation"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    l_of_i = list_of_integers
    length = len(list_of_integers)

    if length > 1:
        if l_of_i[0] >= l_of_i[1]:
            return l_of_i[0]

        if l_of_i[-1] >= l_of_i[-2]:
            return l_of_i[-1]

        for i in range(1, length):
            if l_of_i[i] >= l_of_i[i - 1] \
               and l_of_i[i] >= l_of_i[i + 1]:
                return(l_of_i[i])

    if l_of_i is None:
        return None
