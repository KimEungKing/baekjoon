import sys
input = sys.stdin.readline

# 1 <= n <= 10
dp = [0]* 11 # n max 10
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,11):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
