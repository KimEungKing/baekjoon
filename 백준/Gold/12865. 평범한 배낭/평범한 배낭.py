# 백준 12865
#
# 준서가 버틸 수 있는 무게의 물건 N개 최대 가치
# 제한된 무게 내에서 가장 높은 가치를 뽑아내는 것에 신경 써야 한다
#
# n*k 크기 배열 만들고 dp[n][k]에 가치 저장
# dp[n][k]

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
wv = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*(k+1) for _ in range(n+1)]
# [0,0] ~ [n,k]

for i in range(1,n+1):
    for j in range(1,k+1):  # 무게
        if j >= wv[i-1][0]:
            # i번째 물건의 가치 + 나머지 무게의 이전 가치, 이전 가치 중 최대값 
            dp[i][j] = max(wv[i-1][1]+dp[i-1][j-wv[i-1][0]], dp[i-1][j])
        else:
            # 최대 무게보다 현재 물건의 무게가 더 무거우면 이전의 가치 그대로
            dp[i][j] = dp[i-1][j]

print(dp[n][k])