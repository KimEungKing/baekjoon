import sys
input = sys.stdin.readline

t = int(input())

# n 최대 100
p = [0] * 100
p[0],p[1],p[2] = 1,1,1
for i in range(3, 100):
    p[i] = p[i-3] + p[i-2]

for _ in range(t):
    n = int(input())
    print(p[n-1])