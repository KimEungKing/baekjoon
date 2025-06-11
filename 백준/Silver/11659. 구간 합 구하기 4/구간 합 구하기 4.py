import sys
input = sys.stdin.readline

# n,m 최대 10만
# print(sum(arr[i-1:j])) # 시간 초과
n,m = map(int,input().split())
arr = list(map(int,input().split()))
# 누적합 prefix
sum_arr = [0] * (n+1)
for i in range(1,n+1):
    sum_arr[i] = sum_arr[i-1] + arr[i-1]

for _ in range(m):
    i,j = map(int,input().split())
    print(sum_arr[j] - sum_arr[i-1])    # (j까지의 합) - (i 이전까지의 합)