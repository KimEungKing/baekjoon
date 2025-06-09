import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
s = [i for i in range(n,0,-1)]
answer = []
tmp = []
result = ''

while arr:
    if not tmp:
        tmp.append(s.pop())
        result += '+'

    if tmp[-1] == arr[0]:
        answer.append(tmp.pop())
        arr.pop(0)
        result += '-'
        # print(*answer)
    else:
        if not s:
            result = ""
            break
        tmp.append(s.pop())
        result += '+'
        # print(*tmp)

if not result:
    print('NO')
else:
    for i in range(len(result)):
        print(result[i])