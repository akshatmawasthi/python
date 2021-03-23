#Example 1 of Append & Pop

x = [3,4,5]
x.append(6)
print(x)
x.append(7)
print(x)
x.pop()
print(x)

print("Above is the result of first example")

#Accessing items in a list

x = [3,4,5]

print(x[0])
print(x[1])

print(x[-1])
print("Above is the result of second example")

#Try the exercises below

#Given the list y = [6,4,2] add the items 12, 8 and 4.
#Change the 2nd item of the list to 3.

list = [6,4,2]
list.append(12)
list.append(8)
list.append(4)

list[1] = 3
print(list)
