#!/bin/bash
# get content length
curl -s $1 | wc -c
