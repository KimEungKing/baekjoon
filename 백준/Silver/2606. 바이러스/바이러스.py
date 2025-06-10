import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
e = int(input())
edge = [[] for _ in range(n + 1)]

for _ in range(e):
    start, end = map(int, input().split())
    edge[start].append(end)
    edge[end].append(start)

visited = [False] * (n + 1)


def bfs(s):
    q = deque()
    visited[s] = True
    q.append(s)
    cnt = 0
    while q:
        node = q.popleft()
        for i in edge[node]:
            if not visited[i]:
                q.append(i)
                visited[i] =True
                cnt += 1
    return cnt


print(bfs(1))
