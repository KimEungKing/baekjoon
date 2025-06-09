import sys
input = sys.stdin.readline

# 그리디

n,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]
cnt = 0
i=-1
while i >= -n:
    if k // arr[i] > 0:
        cnt += k // arr[i]
        k = k % arr[i]
    i-=1
print(cnt)