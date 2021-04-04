#Question at https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/743/

n = input()

for i in range(1,n):
  if i%3 == 0 and i%5 == 0:
    print('"buzz"')
  elif i%3 == 0 and i%5 != 0:
    print('"fizz"')
  else:
    print('"'+ str(i) + '"')
