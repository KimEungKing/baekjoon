import sys
input = sys.stdin.readline

n = int(input())
scores = [int(input()) for _ in range(n)]

# n 이 작을 때 예외처리
if n == 0:
    print(0)
elif n == 1:
    print(scores[0])
elif n == 2:
    print(scores[0] + scores[1])
# 본 코드
else:
    # 각 계단을 지나면서 만들 수 있는 최대 점수를 dp로
    dp = [0] * (n)
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1] # 2번째 계단까지는 최대값이 무조건
    dp[2] = max(scores[0]+scores[2],scores[1]+scores[2]) # 1번계단+3번계단 / 2번계단+3번계단 중 큰 값
                                                         # 3번 연속 계단을 밟을 수 없으니까

    for i in range(3,n):
        # 연속 2칸까지 오를 수 있으니까
        # dp[i]의 값이 연속 2칸 오를때 큰지, 2칸 한번에 오른게 큰지
        dp[i] = max(dp[i-3] + scores[i-1] + scores[i], dp[i-2]+scores[i])

    print(dp[n-1])
