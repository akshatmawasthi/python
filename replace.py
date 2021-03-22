# Try the replace program
# Can a string be replaced twice?
# Does replace only work with words or also phrases?

s = "Hello World World World"
s = s.replace("World", "Universe", 1)

print(s)

s = " A B C D"
s = s.replace("B", "C")
s = s.replace("B", "D")

print(s)

s = "Trying this out with phrase"
s = s.replace("Trying this out with phrase", "Replacing old phrase")

print(s)
