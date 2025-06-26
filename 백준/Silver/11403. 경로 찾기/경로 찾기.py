import sys
input = sys.stdin.readline
from collections import deque

# 방향 그래프
n = int(input())
arr = [[] for _ in range(n)]

for k in range(n):
    tmp = list(map(int,input().split()))
    for i in range(len(tmp)):
        if tmp[i] == 1:
            arr[k].append(i)

answer = [[0]*n for _ in range(n)]
q = deque()
for i in range(n):
    q.append(i)
    visited = [False] * n
    while q:
        t = q.popleft()
        for nxt in arr[t]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                answer[i][nxt] = 1

for i in answer:
    print(*i)