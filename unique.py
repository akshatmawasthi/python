#Question at https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/

s = "aabbcc"
n = 0
while n < len(s):

  if s[n] != s[n+1]:
    print(s[n])
    break
  else:
    break

n = n + 1
