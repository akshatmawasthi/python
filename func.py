# 1. Make a function that sums the list mylist = [1,2,3,4,5]
# 2. Can functions be called inside a function?
# 3. Can a function call itself? (hint: recursion)
# 4. Can variables defined in a function be used in another function? (hint: scope)

mylist = [1,2,3,4,5]
def sumlist():
    for i in mylist:
        while i in range(1,len(mylist)):
            sum = mylist[i-1] + mylist[i]
            print(sum)
            i = i + 1
m = 4
sumlist()

def sum(a,b):
    sumr = a + b
    print(sumr)
    global m
    m = 4

def mul(c,d):
    mul = m * d
    print(mul)

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

print(mul(m,4))
num = 100
print("The factorial of", num, "is", factorial(num)

)
