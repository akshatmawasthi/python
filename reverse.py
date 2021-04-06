#Question at https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

s = str(input())

arr = list(s)

n = len(arr) - 1
r = []

while n >= 0:
  j = (arr[n])
  r.append(j)
  n = n-1

print(r)

