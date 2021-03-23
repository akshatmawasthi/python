#Try the exercises below

#Create a list of one thousand numbers
#Get the largest and smallest number from that list
#Create two lists, an even and odd one.

thousand = range(0,1000)
print(thousand[0])
print(thousand[-1])

for x in thousand:
    if x % 2 == 0:
        print("Even", x)
    else:
        print("Odd", x)
