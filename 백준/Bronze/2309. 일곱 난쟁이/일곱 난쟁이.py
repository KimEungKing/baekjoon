import random
import sys
input = sys.stdin.readline

# 난쟁이 키 합 100
arr = [int(input()) for _ in range(9)]
arr.sort()

# 랜덤 셔플로 해도 통과 될거같은데
res = []
while True:
    random.shuffle(arr)
    tmp = sum(arr[:7])
    if tmp == 100:
        res = arr[:7]
        break

for i in sorted(res):
    print(i)
