import sys
input = sys.stdin.readline

# 1, 3, 5, 11
# f(n) = f(n-1) + 2*f(n-2)
dp = [0] * (1001)
dp[1] = 1
dp[2] = 3
for i in range(3,1001):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007

n = int(input())
print(dp[n])