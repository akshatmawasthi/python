print("First Example - Sorting a list")

x = [3,6,21,1,5,98,4,23,1,6]
x.sort()
print(x)

print("Second Example - Sorting strings")

words = ["Be","Car","Always","Door","Eat" ]
words.sort()
print(words)

print("Third Example - Reverse Sort")
x = [3,6,21,1,5,98,4,23,1,6]
x.sort()
x = list(reversed(x))
print(x)

#Given a list with pairs, sort on the first element

#x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]
#Now sort on the second element

y = [ (3,6),(4,7),(5,9),(8,4),(3,1)]

print(sorted(y, key = lambda x:x[0]))

print(sorted(y, key = lambda x:x[1]))
