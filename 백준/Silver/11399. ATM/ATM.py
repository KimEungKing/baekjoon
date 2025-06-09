import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
answer = 0
tmp = 0
for i in arr:
    tmp += i
    answer += tmp

print(answer)