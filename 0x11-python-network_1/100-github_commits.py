#!/usr/bin/python3
"""Shows the last 10 commits via Github API"""
from requests import get
from sys import argv

if __name__ == "__main__":
        try:
                url = get("https://api.github.com/repos/{}/{}/commits".format(
                        argv[2], argv[1])).json()
                for i in range(0, 10):
                        print("{}: {}".format(url[i].get("sha"),
                                              url[i].get("commit").get(
                                                      "author").get("name")))
        except:
                pass
