import sys
input = sys.stdin.readline
import heapq

n = int(input())
max_heap = []
min_heap = []

for _ in range(n):
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap,(-1)*int(input()))
    else:
        heapq.heappush(min_heap,int(input()))

    if min_heap and -max_heap[0] > min_heap[0]:
        temp_min = heapq.heappop(min_heap)
        temp_max = heapq.heappop(max_heap)
        heapq.heappush(max_heap, -temp_min)
        heapq.heappush(min_heap, -temp_max)

    print(-max_heap[0])

