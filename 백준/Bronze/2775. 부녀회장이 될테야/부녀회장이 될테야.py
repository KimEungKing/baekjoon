import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    arr = [[1]*n for _ in range(k+1)]
    for i in range(len(arr[0])):
        arr[0][i] = i + 1

    for i in range(1,len(arr)):
        for j in range(1,len(arr[0])):
            arr[i][j] = arr[i][j-1]+arr[i-1][j]

    print(arr[k][n-1])
# 1  4  10 20 35
# 1  3  6  10 15
# 1  2  3  4  5