import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
k = int(input())

for _ in range(k):
    i,j,x,y = map(int,input().split())

    answer = 0
    for t in range(i-1,x):
        answer += sum(arr[t][j-1:y])
        
    print(answer)
