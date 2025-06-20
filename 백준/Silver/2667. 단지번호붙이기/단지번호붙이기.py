import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = [list(map(int,input().rstrip())) for _ in range(n)]

dy,dx = [-1,0,1,0],[0,1,0,-1] # N, E, S, W
visited = [[False]*n for _ in range(n)]
q = deque()
x = y = cnt = 0

house = deque()

for i in range(n):
    for j in range(n):
        if arr[j][i] != 0 and not visited[j][i]:
            hc = 1
            q.append((i,j))
            visited[j][i] = True
            
            while q:
                x,y = q.popleft()
                for d in range(4):
                    ny = y+dy[d]
                    nx = x+dx[d]
                    if 0 <= ny < n and 0 <= nx < n:
                        if arr[ny][nx] != 0 and not visited[ny][nx]:
                            visited[ny][nx] = True
                            q.append((nx, ny))
                            hc += 1
            cnt += 1
            house.append(hc)

print(cnt)
for i in sorted(house):
    print(i)
