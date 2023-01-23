#!/usr/bin/python3
"""The script takes two command line arguments, a username and a password,
and creates an HTTPBasicAuth object with it. It then makes a GET request 
to the GitHub API endpoint "https://api.github.com/user" passing the auth object.
It then extracts the 'id' from the json response and prints it
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
   #getting the username and password from command line arguments
    username = sys.argv[1] 
    password = sys.argv[2]

    # Creating an HTTPBasicAuth object 
    auth = HTTPBasicAuth(username, password)

    # Making a GET request to the url with auth
    r = requests.get("https://api.github.com/user", auth=auth)

    #Getting the 'id' from the json response
    print(r.json().get("id"))
