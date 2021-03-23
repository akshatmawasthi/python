# Can try-except be used to catch invalid keyboard input?
# Can try-except catch the error if a file can’t be opened?

try:
    x = input("Enter number x: ")
    x = x + 1
    print(x)

except:
    print("Invalid input, enter a number")


try: 
    f = open("test.txt")
except: 
    print('Could not open file')
finally:
    f.close()

print('Program continue')
