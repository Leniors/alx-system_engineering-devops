#!/bin/bash
# body
#curl -s -w "%{http_code}" $1

response=$(curl -s -w "%{http_code}" "$1")
if [ "${response: -3}" == "200" ]; then
	curl -s $1
fi
