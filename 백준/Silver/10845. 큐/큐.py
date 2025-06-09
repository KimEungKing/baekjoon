import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque()
for _ in range(n):
    order = input().rstrip().split()
    if order[0] == 'push':
        q.append(order[1])

    elif order[0] == 'pop':
        if not q:
            print(-1)
            continue
        print(q.popleft())

    elif order[0] == 'size':
        print(len(q))

    elif order[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)

    elif order[0] == 'front':
        if not q:
            print(-1)
            continue
        print(q[0])
    elif order[0] == 'back':
        if not q:
            print(-1)
            continue
        print(q[-1])

