import sys
input = sys.stdin.readline
from collections import deque

# 시작점에서 각 노드들과의 거리의 합이 가장 작은 거 구하기

n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

# bfs 
kevin = 5001
answer = 0
# 만약 합이 같으면 수가 작은 걸 출력하기 위해 역순으로 시작 
for i in range(n,0,-1):
    visited = [False] * (n + 1)
    q = deque()
    q.append(i)
    visited[i] = True
    dist = [0]*(n+1) # 시작노드인 i와 각 노드별 거리

    while q:
        t = q.popleft()
        for j in arr[t]:
            if not visited[j]:
                visited[j] = True
                dist[j] = dist[t] + 1
                q.append(j)
    s = sum(dist)
    if kevin >= s:
        kevin = s
        answer = i

print(answer)
