import sys
input = sys.stdin.readline
from collections import deque

# bfs
t = int(input())
dx, dy = [1,0,-1,0],[0,1,0,-1]
for _ in range(t):
    m,n,k = map(int,input().split())
    arr = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        arr[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                q = deque()
                q.append((i,j))
                while q:
                    a,b = q.popleft()
                    for d in range(4):
                        nx = a + dx[d]
                        ny = b + dy[d]
                        if 0 <= nx < n and 0 <= ny < m:
                            if arr[nx][ny] == 1 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append((nx, ny))

    print(cnt)