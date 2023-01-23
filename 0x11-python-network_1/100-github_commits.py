#!/usr/bin/python3
"""The script takes two command line arguments, a username and a 
repository name, and creates a url by formatting it with them, 
then makes a GET request to that url using the requests library. 
It then extracts the first 10 commits, gets the SHA and name of the 
author of each commit, and prints the SHA and name of each commit. 
If there are less than 10 commits, it will not raise an error and 
just print the available commits
"""
import sys
import requests


if __name__ == "__main__":
        url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])

        # Making a GET request to the url
        r = requests.get(url)

        #parsing the json response
        commits = r.json()

        try:
            #iterating through the first 10 commits
            for i in range(10):
                #Getting the sha and name of the author of the commit
                sha = commits[i].get("sha")
                name = commits[i].get("commit").get("author").get("name")
                #printing the sha and name
                print("{}: {}".format(sha, name))
        except IndexError:
            #passing if the index is out of range
            pass
