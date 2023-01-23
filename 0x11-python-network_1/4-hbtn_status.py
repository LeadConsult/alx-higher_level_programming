#!/usr/bin/python3
"""The script makes a GET request to the URL "https://alx-intranet.hbtn.io/status" 
using the requests library, then it prints the type and content of the response
"""
import requests


if __name__ == "__main__":
    # Making a GET request to the url
    r = requests.get("https://alx-intranet.hbtn.io/status")

    # Printing information about the response
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
