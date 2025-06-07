import sys
input = sys.stdin.readline
from collections import deque
# queue
n = int(input())
q = deque(range(1,n+1))

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(*q)