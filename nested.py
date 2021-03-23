#!/usr/bin/python

# Try the exercises below

# Given a tic-tac-toe board of 3x3, print every position

# Create a program where every person meets the other
#persons = [ “John”, “Marissa”, “Pete”, “Dayton” ]

xax = [1,2,3]
yax = [1,2,3]

for x in xax:
    for y in yax:
        print(x, y)

persons = ["John", "Marissa", "Pete", "Dayton"]

for p in persons:
    for r in persons:
        if p != r:
            print(p,r)
