#!/usr/bin/python3
"""Uses the Github API to display your id"""
from requests import get
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    r = get(url, auth=(argv[1], argv[2])).json()

    try:
        print(r["id"])
    except:
        print("No results")
