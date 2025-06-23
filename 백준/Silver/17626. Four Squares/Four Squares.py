import sys
input = sys.stdin.readline

# dp로 풀기
# n 최대 5만
# dp[i] : i 의 제곱수 표현 최소 개수 ?
# ex) dp[26] == 2
# dp[1] == 1 , dp[2] == 2, dp[3] == 3, dp[4] == 1, ...

n = int(input())
dp = [i for i in range(n+1)]

for i in range(1,n+1):
    # 시간초과 남 
    # for j in range(1,int((n+1)**0.5)+1):
    # j 는 i보다 작거나 같은 수만 판단하면 된다
    for j in range(1,int(i**0.5)+1):
        # 제곱수를 1개 빼고, 가장 적은 개수
        # ex) 26 --> j가 5일 때, dp[1] + 1 == 2
        dp[i] = min(dp[i], dp[i-j*j] + 1)

print(dp[n])