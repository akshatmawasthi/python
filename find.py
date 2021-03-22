# Try the exercises below

# Find out if string find is case sensitive
# What if a query string appers twice in the string?
# Write a program that asks console input and searches for a query.

s = "Hi, my name is Akshat"
index = s.find("akshat")
print(index)

t = "Hi, my name is Akshat Akshat"
index2 = t.find("Akshat")
print(index2)

r = input() 
index3 = r.find("Akshat")
print(index3)
