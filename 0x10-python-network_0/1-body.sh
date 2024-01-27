#!/bin/bash
# body
response=$(curl -s -w "%{http_code}" $1) && [ "${response: -3}" == "200" ] && curl -s $1
