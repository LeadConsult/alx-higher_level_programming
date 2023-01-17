#!/bin/bash
# Retrieve and display all the HTTP methods accepted by the server of a specific URL.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
