import sys
input = sys.stdin.readline
from collections import defaultdict
# 경우의 수
# 카테고리별로 옷의 개수를 세서 곱하기 ( 아무것도 안입은 상태 포함 )
t = int(input())
for _ in range(t):
    n = int(input())
    clothes = defaultdict(int)

    for _ in range(n):
        name, category = input().rstrip().split()
        clothes[category] +=1

    answer = 1
    for i in clothes:
        answer *= clothes[i]+1
    answer -= 1 # 다 벗은 경우 제외
    print(answer)