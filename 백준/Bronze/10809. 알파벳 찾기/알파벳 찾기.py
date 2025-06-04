import sys
input = sys.stdin.readline

s = input().rstrip()
arr = [-1]*26
for i in range(len(s)):
    if arr[ord(s[i])-97] == -1:
        arr[ord(s[i])-97] = i
print(*arr)