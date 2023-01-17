#!/bin/bash
# Retrieve the byte size of the HTTP response header for a specific URL.
curl -s "$1" | wc -c
