import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
preSum = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        preSum[i][j] = arr[i-1][j-1] + preSum[i-1][j] + preSum[i][j-1] - preSum[i-1][j-1]

answer = 0
for _ in range(k):
    i, j, x, y = map(int, input().split())

    answer = preSum[x][y] - preSum[i-1][y] - preSum[x][j-1] + preSum[i-1][j-1]

    print(answer)
