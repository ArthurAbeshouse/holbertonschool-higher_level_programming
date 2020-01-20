#!/usr/bin/python3


class MyInt(int):
    def __eq__(self, other):
        """override equals, inverting it"""
        return int(self) != int(other)

    def __ne__(self, other):
        """override not-equals, inverting it"""
        return int(self) == int(other)
