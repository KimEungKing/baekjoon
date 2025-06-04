import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    r,s = input().split()
    result = ''
    for i in range(len(s)):
        result += int(r)*s[i]
    print(result)