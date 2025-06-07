import sys
input = sys.stdin.readline

k = int(input())
s = []
tmp = 0
for i in range(k):
    tmp = int(input())
    if tmp != 0:
        s.append(tmp)
    else:
        s.pop()

print(sum(s))