import sys
input = sys.stdin.readline

# n 최대 3,000,000
# set 사용
s = set()
m = int(input())
for _ in range(m):
    tmp = input().rstrip().split()
    if tmp[0] == 'add':
        s.add(int(tmp[1]))
    elif tmp[0] == 'remove':
            s.discard(int(tmp[1]))
    elif tmp[0] == 'check':
        if int(tmp[1]) in s:
            print(1)
        else:
            print(0)
    elif tmp[0] == 'toggle':
        if int(tmp[1]) in s:
            s.discard(int(tmp[1]))
        else:
            s.add(int(tmp[1]))
    elif tmp[0] == 'all':
        s = set(range(1,21))
    elif tmp[0] == 'empty':
        s = set()
        # s.clear()

