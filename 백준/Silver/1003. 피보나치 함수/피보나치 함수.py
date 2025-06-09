import sys
input = sys.stdin.readline
# n == 40
# 피보나치 함수 O(2^n), 2**40 == 1099511627776
# dp 로 풀어야함
# ----------------------------------------
#         수  0  1  2  3  4  5  6  7
# 0 호출 횟수 : 1  0  1  1  2  3  5  8      f(n-2) + f(n-1) = f(n)
# 1 호출 횟수 : 0  1  1  2  3  5  8  13     g(n-2) + g(n-1) = g(n)

dp = [(1,0),(0,1)] + [0] * 39
for i in range(2,41):
    dp[i] = (dp[i-2][0] + dp[i-1][0],dp[i-2][1] + dp[i-1][1])

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n][0],dp[n][1])

