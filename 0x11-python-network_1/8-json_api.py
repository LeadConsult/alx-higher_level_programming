#!/usr/bin/python3
"""The script takes one command line argument, a letter,
and creates a payload with it. It then makes a POST request 
to the endpoint "http://0.0.0.0:5000/search_user" with the payload. 
It then tries to parse the response into JSON, if the response is 
empty it prints a message of "No result", if the response is not empty 
it prints the id and name of the user. If the response is not a valid JSON 
it prints a message "Not a valid JSON".
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1] #getting the letter from command line argument
    payload = {"q": letter} # creating the payload to send in the POST request

    #Making a POST request to the url with data
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        #parsing the response into json
        response = r.json()
        if response == {}:
            #Printing the no result message if the response is empty
            print("No result")
        else:
            #Printing the id and name of the user
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        #Printing the message if the response is not a valid JSON
        print("Not a valid JSON")
