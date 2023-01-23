#!/usr/bin/python3
"""The script takes the URL and an email address 
from command line arguments, creates
a dictionary with email value, makes a POST 
request to the URL with the data, and prints the response content
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1] #Getting the URL from command line arguments
    value = {"email": sys.argv[2]} #Creating a dictionary with email value

    #Making a POST request to the url with data
    r = requests.post(url, data=value)

    #Printing the response content
    print(r.text)
