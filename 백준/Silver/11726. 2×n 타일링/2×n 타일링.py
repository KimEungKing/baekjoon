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

# n = int(input())
# if n == 1:
#     print(1)
# elif n ==2:
#     print(2)
# else:
#     dp = [0] * (n+1)
#     dp[1] = 1
#     dp[2] = 2
#     for i in range(3,n+1):
#         dp[i] = (dp[i-1] + dp[i-2]) % 10007
#     print(dp[n])
