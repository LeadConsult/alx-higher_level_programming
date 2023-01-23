#!/usr/bin/python3
"""The script takes the URL from command line arguments,
creates a request object and opens the URL, 
reading the response, it then extracts the value of 
the X-Request-Id header, and prints it.
"""
import sys
import urllib.request


if __name__ == "__main__":
    #Getting the URL from command line arguments
    url = sys.argv[1]

    # Creating request object
    request = urllib.request.Request(url)
    # Opening the url and reading the response
    with urllib.request.urlopen(request) as response:
        # Getting the value of X-Request-Id header
        x_request_id = dict(response.headers).get("X-Request-Id")
        # Printing the value of X-Request-Id
        print(x_request_id)
