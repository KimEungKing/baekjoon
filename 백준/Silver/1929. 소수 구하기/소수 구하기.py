import sys
input = sys.stdin.readline

m, n = map(int,input().split())
arr = [x for x in range(n+1)]
arr[1] = 0 # 1은 소수 아님

# 에라토스테네스의 체
for i in range(2,int(n**0.5) + 1):
    if arr[i] != 0:
        for j in range(i*i,n+1,i):
            arr[j] = 0

for i in range(m,n+1):
    if arr[i] != 0:
        print(i)