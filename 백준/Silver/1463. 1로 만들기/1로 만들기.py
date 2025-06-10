import sys
input = sys.stdin.readline

# n 최대 100만
n = int(input())
dp = [0] * (n+1)

# 인덱스를 숫자로 쓰고, dp[i]를 숫자 i 를 1로 만들기위한 최소 연산
for i in range(2,n+1):
    dp[i] = dp[i-1]+1   # ex) 3이 2가 되려면 1번의 연산 필요

    if i%2 == 0:
        # 2로 나눠지면, 2로 나눈 값에서 1로가는 최소 값에 연산횟수 1을 더해서 현재 값 중 작은 것 선택
        dp[i] = min(dp[i],dp[i//2]+1)
    # 2로 나눈 나머지가 3으로도 나눠질 수 있으니 elif 대신 if
    if i%3 == 0:
        dp[i] = min(dp[i],dp[i//3]+1)

print(dp[n])

