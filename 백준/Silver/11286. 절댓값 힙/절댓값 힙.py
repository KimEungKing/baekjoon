import sys
input = sys.stdin.readline
import heapq

n = int(input())
h = []
heapq.heapify(h)

for _ in range(n):
    x = int(input())

    if x == 0:
        if not h:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    else:
        heapq.heappush(h, (abs(x),x))
