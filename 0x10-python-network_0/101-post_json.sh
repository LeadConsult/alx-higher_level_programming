#!/bin/bash
# Execute a POST request with a JSON payload to a specific URL using a specified JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
