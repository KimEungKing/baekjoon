import sys
input = sys.stdin.readline

# 1, 2, 3, 5, 8 ,,,,
# f(n) = f(n-1) + f(n-2)
dp = [0] * 1001
dp[1], dp[2], dp[3] = 1,2,3
for i in range(4,1001):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

n = int(input())

print(dp[n])
