#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter"""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    data = parse.urlencode({"email": argv[2]}).encode()
    request = request.Request(argv[1], data)
    with request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
