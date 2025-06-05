import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().split()) for _ in range(n)]
# int(x[0]) 안해주면 사전순이라 '100' < '2' 
arr.sort(key = lambda x:int(x[0]))

for i in range(n):
    print(*arr[i])