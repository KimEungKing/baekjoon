import sys
input = sys.stdin.readline

l = int(input())
s = input().rstrip()
result = 0
# a의 ascii 97
for i in range(len(s)):
    result += (ord(s[i])-96)*(31 ** i)
print(result)