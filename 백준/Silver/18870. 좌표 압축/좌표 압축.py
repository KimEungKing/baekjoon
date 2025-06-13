import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 작은 숫자대로 번호 매기기
tmp = sorted(set(arr))
zipped = {num: idx for idx, num in enumerate(tmp)}

answer = []
for i in arr:
    answer.append(zipped[i])
print(*answer)
