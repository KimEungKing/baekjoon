import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    q = deque(enumerate(map(int,input().split())))

    cnt = 0
    tmp = 0
    while True:
        if q[0][1] >= max(x[1] for x in q):
            tmp = q.popleft()
            cnt += 1
            if tmp[0] == m:
                break
        else:
            q.append(q.popleft())
    print(cnt)
