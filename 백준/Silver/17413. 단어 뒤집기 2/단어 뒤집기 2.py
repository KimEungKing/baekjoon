import sys
input = sys.stdin.readline

s = input().rstrip()
answer = ''
stk = []
judge = False

# 괄호열렸으면 닫힐때까지 answer에 추가
for i in s:

    if i == '<':
        judge = True
        for _ in range(len(stk)):
            answer += stk.pop()
        stk.append(i)

    elif i == '>':
        judge = False
        stk.append(i)
        for _ in range(len(stk)):
            answer += ''.join(stk)
            stk.clear()

    elif i == ' ' and not judge:
        for _ in range(len(stk)):
            answer += stk.pop()
        answer += ' '
    else:
        stk.append(i)
if stk:
    for _ in range(len(stk)):
        answer += stk.pop()

print(answer)