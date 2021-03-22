# 1. Make a program that lists the countries in the set below using a while loop.

clist = ["Canada","USA","Mexico"]
# 2. What’s the difference between a while loop and a for loop?
# 3. Can you sum numbers in a while loop?
# 4. Can a for loop be used inside a while loop?

clist = ["Canada", "USA", "Mexico"]
size = len(clist)

i = 0
while i < size:
   print(clist[i])
   i = i + 1

a = 50

while a < 51:
    for a in range (1,50):
        print(a, "ok")
        a = a + 1
