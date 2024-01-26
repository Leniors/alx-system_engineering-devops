#!/bin/bash
# allow
curl -sI $1 | awk '/^Allow:/ {print substr($0, 8)}'
