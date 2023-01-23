#!/usr/bin/python3
"""The script takes one command line argument, the URL,
and makes a GET request to that URL using the requests library. 
It then checks the status code of the response and prints the 
error code if the status code is greater than or equal to 400. 
If the status code is less than 400, it prints the response content
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1] #Getting the URL from command line arguments

    #Making a GET request to the url
    r = requests.get(url)

    #Checking the status code of the response
    if r.status_code >= 400:
        #Printing the error code if the status code is greater than or equal to 400
        print("Error code: {}".format(r.status_code))
    else:
        #Printing the response content if the status code is less than 400
        print(r.text)
