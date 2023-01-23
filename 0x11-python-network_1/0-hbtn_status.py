#!/usr/bin/python3
"""The script makes a request to "https://alx-intranet.hbtn.io/status"
using urllib, then reads and stores the response, printing the type,
content, and utf-8 content of the response.
"""
import urllib.request


if __name__ == "__main__":
         # Making request to the url using Request object
        request = urllib.request.Request("https://alx-intranet.hbtn.io/status")

        # Opening the url and reading the response
        with urllib.request.urlopen(request) as response:
            # Storing the response in a variable
            body = response.read()

         # Printing information about the response
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
