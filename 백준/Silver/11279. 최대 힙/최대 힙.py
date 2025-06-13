import sys

input = sys.stdin.readline

import heapq
# heapq 는 최소힙 구조
# heap에 들어갈 원소를 -로 부호를 바꿔주고 꺼낼때 다시 -를 곱해서 
# 최대힙으로 사용 

n = int(input())
h = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if not h:
            print(0)
        else:
            print(-heapq.heappop(h))
    elif x > 0:
        heapq.heappush(h, -x)
