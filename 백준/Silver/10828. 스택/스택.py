import sys
input = sys.stdin.readline

n = int(input())
s = []
for _ in range(n):
    order = input().rstrip().split()
    if order[0] == 'push':
        s.append(order[1])

    elif order[0] == 'pop':
        if not s:
            print(-1)
            continue
        print(s.pop())

    elif order[0] == 'size':
        print(len(s))

    elif order[0] == 'empty':
        if s:
            print(0)
        else:
            print(1)

    elif order[0] == 'top':
        if not s:
            print(-1)
            continue
        print(s[-1])

