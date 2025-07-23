import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for _ in range(n):
    s = input().rstrip()
    arr = [s[0]]
    cnt = 0
    for i in s:
        if i != arr[-1]:
            arr.append(i)
    cnt = len(arr)

    if cnt == len(set(arr)):
        answer += 1
    else:
        continue
print(answer)