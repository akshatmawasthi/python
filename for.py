# 1. Make a program that lists the countries in the set

# clist = ['Canada','USA','Mexico','Australia']
# 2. Create a loop that counts from 0 to 100
# 3. Make a multiplication table using a loop
# 4. Output the numbers 1 to 10 backwards using a loop
# 5. Create a loop that counts all even numbers to 10
# 6. Create a loop that sums the numbers from 100 to 200

clist = ['Canada','USA','Mexico','Australia']

for x in clist:
    print(x)

score = range(1,101)
for y in score:
    print(y)

mult = range(1,11)

for z in mult:
    print(z*2)

for a in mult:
    print(10 - a)

for b in mult:
    if b < 6:
        print(b*2)

num = 100
for i in range (99, 200):
    num = num + i 
print(num)
