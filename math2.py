#Question at https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/
n = int(input())
count = 0

for i in range(2,n):
  if (i%n) == 0:
    break
  else:
    count = count + 1

print(count)
