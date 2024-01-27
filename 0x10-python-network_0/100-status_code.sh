#!/bin/bash
# status code
response=$(curl -s -w "%{http_code}" "$1") && status_code="${response: -3}" && echo "$status_code"
