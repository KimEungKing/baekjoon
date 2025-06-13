import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(n)]

doyeon = []
for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            doyeon = (j, i)

# bfs
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
visited = [[False] * m for _ in range(n)]

q = deque()
q.append(doyeon)
visited[doyeon[1]][doyeon[0]] = True
answer = 0
while q:
    x, y = q.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < m and 0 <= ny < n:
            if not visited[ny][nx] and campus[ny][nx] != 'X':
                visited[ny][nx] = True
                q.append((nx, ny))
                if campus[ny][nx] == 'P':
                    answer += 1
print(answer if answer != 0 else 'TT')