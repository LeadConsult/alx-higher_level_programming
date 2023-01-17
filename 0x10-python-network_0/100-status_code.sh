#!/bin/bash
# Execute a GET request to a specific URL and display the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
