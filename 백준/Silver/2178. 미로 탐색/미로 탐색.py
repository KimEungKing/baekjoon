import sys
input = sys.stdin.readline
from collections import deque

# 최단거리 bfs
n,m = map(int,input().split())
arr = [list(map(int,input().rstrip())) for _ in range(n)]

dy,dx = [-1,0,1,0],[0,1,0,-1] # N, E, S, W
visited = [[False]*m for _ in range(n)]
q = deque()
q.append((0,0,1))
x = y = t = 0

while q:
    x,y,t = q.popleft()
    if x == m-1 and y == n-1:
        print(t)
        break

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0 <= ny < n and 0 <= nx < m:
            if arr[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny,t+1))

