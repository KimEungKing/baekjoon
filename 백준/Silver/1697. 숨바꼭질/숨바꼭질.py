import sys
from collections import deque

input = sys.stdin.readline

# 현재위치 x
# if 걷기 : 1초 후에 x-1 or x+1
# if 순간이동 : 1초 후 2*x
# n -> k 까지 가는 가장 빠른 시간
# n, k 최대 10만

n, k = map(int, input().split())

# bfs
x = n
visited = [False] * 100001
q = deque()
q.append((x, 0)) # (현재위치, 걸린시간) 으로 넣기
while q:
    x, t = q.popleft()
    if x == k:
        print(t)
        break
    if 0 <= x <= 100000:
        if not visited[x]:
            visited[x] = True
            q.append((x - 1,t+1)) # 모든 횟수를 세는 것이 아닌 
            q.append((x + 1,t+1)) # 깊이당 1씩 추가 
            q.append((x * 2,t+1))
