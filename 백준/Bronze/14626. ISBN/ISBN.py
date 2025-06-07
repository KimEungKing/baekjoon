import sys
input = sys.stdin.readline

n = input().rstrip()

m = int(n[-1])
target = 0
tmp = 0
for i in range(1,len(n)):
    if n[i-1] == '*':
        if i % 2 == 0:
            target = 3
        else:
            target = 1
    else:
        if i%2 == 0:
            tmp += 3 * int(n[i-1])
        else:
            tmp += int(n[i-1])

for i in range(10):
    if (m + tmp + i*target) % 10 == 0:
        print(i)
        break