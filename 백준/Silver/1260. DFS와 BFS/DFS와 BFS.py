import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
edge = [[] for _ in range(N + 1)]  # 입력 노드 번호 이용하기 위해 N+1

for _ in range(M):
    start, end = map(int, input().split())
    edge[start].append(end)
    edge[end].append(start)  # 각 노드 양방향으로 연결
for i in range(len(edge)):
    edge[i].sort()

def dfs(v):
    visited.append(v)
    for i in edge[v]:
        if i in visited:
            continue
        else:
            dfs(i)

def bfs(v):
    q = deque()
    visited.append(v)
    q.append(v)
    while q:
        tmp = q.popleft()
        for i in edge[tmp]:
            if i not in visited :
                visited.append(i)
                q.append(i)


visited = []
dfs(V)
print(*visited)

visited = []
bfs(V)
print(*visited)