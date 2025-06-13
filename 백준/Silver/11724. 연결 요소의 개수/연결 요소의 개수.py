import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [False] * (n + 1)


def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = True
    while q:
        t = q.popleft()
        for nxt in arr[t]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)


# 연결된 요소 개수 구하기
# 노드의 개수만큼 돌리면서 연결된 노드들을 방문처리,
# 첫 방문하는 노드의 개수 세기
cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
