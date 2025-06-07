import sys
input = sys.stdin.readline
# n,m이 크니까 Counter 사용
from collections import Counter

n = int(input())
n_arr = list(map(int,input().split()))
m = int(input())
m_arr = list(map(int,input().split()))

counter = Counter(n_arr)
answer = [counter[i] for i in m_arr]

print(*answer)