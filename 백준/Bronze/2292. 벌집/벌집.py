import sys
input = sys.stdin.readline

N = int(input())
# 각 레이어의 개수 1, 6, 12, 18 ...
# 19 번까지 레이어 3개
# 37 번까지 레이어 4개 .......
# Num += 6*i . if num > n: break
num = 1
i = 1
while num < N :
    num += 6*i
    i += 1

print(i)
