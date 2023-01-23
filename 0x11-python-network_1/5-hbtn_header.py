#!/usr/bin/python3
"""The script takes the URL from command line arguments, makes a GET request 
to that URL using the requests library, then it extracts the value of the 
X-Request-Id header and prints it
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
