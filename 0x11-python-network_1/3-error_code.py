#!/usr/bin/python3
"""creates a request object, opens the URL and reads the response, 
decodes and prints it. In case of a HTTPError, 
it handles it by printing the error code.
"""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
      url = sys.argv[1] #Getting the URL from command line arguments

      # Creating request object
      request = urllib.request.Request(url)

      try:
          # Opening the url and reading the response
          with urllib.request.urlopen(request) as response:
              # Decoding the response and printing it
              print(response.read().decode("ascii"))
      except urllib.error.HTTPError as e:
          # Handling the HTTPError and printing the error code
          print("Error code: {}".format(e.code))
