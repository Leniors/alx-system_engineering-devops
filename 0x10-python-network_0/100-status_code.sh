#!/bin/bash
# status code
echo "$(curl -s -w "%{http_code}" "$1"i: -3)"
