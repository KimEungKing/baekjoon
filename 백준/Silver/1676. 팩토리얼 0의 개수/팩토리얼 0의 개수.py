import sys
input = sys.stdin.readline
import math

n = int(input())
cnt = 0
s = str(math.factorial(n))

for i in range(len(s)-1,-1,-1):
    if s[i] == '0':
        cnt += 1
    else: 
        break
print(cnt)