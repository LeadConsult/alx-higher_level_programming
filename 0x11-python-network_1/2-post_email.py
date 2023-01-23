#!/usr/bin/python3
"""The script takes the URL and an email address from command line
arguments, encodes the data to be sent in the request, 
creates a request object with the data, opens the URL, reads the response, 
decodes it, and prints the response.
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
          url = sys.argv[1] #Getting the URL from command line arguments
          value = {"email": sys.argv[2]} #Creating a dictionary with email value

          # Encoding the data to be sent in the request
          data = urllib.parse.urlencode(value).encode("ascii")

          # Creating request object with data to be sent
          request = urllib.request.Request(url, data)

          # Opening the url and reading the response
          with urllib.request.urlopen(request) as response:
              # Decoding the response and printing it
              print(response.read().decode("utf-8"))
