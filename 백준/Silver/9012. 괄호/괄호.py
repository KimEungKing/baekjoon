import sys
input = sys.stdin.readline
from collections import deque
t = int(input())
for _ in range(t):
    s = input().rstrip()
    q = deque()
    for i in s:
        if i == '(':
            q.append(i)
        else:
            if not q:
                q.append(1)
                break
            q.pop()

    if q:
        print('NO')
    else:
        print("YES")
