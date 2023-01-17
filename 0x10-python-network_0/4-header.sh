#!/bin/bash
# Execute a GET request to a specific URL including a header variable.
curl -sH "X-School-User-Id: 98" "$1"
