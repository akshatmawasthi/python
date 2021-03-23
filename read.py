#!/usr/bin/env python

filename = "your file's name in the same directory"

with open(filename) as f:
    content = f.readlines()

print(content)
