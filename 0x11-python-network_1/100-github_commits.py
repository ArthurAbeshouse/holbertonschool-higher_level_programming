#!/usr/bin/python3
"""Uses the Github API to display your id"""
from requests import get
from sys import argv

if __name__ == "__main__":
        url = get("https://api.github.com/repos/{}/{}/commits".format(
                argv[2], argv[1])).json()
        for i in url:
            print("{}: {}".format(i.get("sha"),
                                  i.get("commit").get("author").get("name")))
