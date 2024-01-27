#!/bin/bash
# body
response=$(curl -s -w "%{http_code}" "$1") && body="${response:0:${#response}-3}" && echo "$body"
