import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    ox = input()
    cnt = 0
    result = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)