import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]
dx,dy = [1,0,-1,0],[0,1,0,-1]
x = y = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            x,y = j,i

q = deque()
q.append((x,y))
arr[y][x] = 0   # 첫 시작 0으로 
visited[y][x] = True
while q:
    x,y = q.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < m and 0 <= ny < n:
            if not visited[ny][nx] and arr[ny][nx] != 0:
                visited[ny][nx] = True
                q.append((nx,ny))
                # 다음 땅들은 거리 +1 
                arr[ny][nx] = arr[y][x] + 1

# 원래 땅이었으나 방문 못한 곳 -1 
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1 :
            arr[i][j] = -1

for i in arr:
    print(*i)