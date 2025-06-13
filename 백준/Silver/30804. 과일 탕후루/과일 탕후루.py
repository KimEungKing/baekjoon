import sys

input = sys.stdin.readline
from collections import Counter

n = int(input())
fruits = list(map(int, input().split()))
start = 0
answer = 0
counter = Counter()

# 슬라이딩 윈도우
# 오른쪽 포인터를 늘려가면서
for end in range(n):
    # 과일 종류별로 카운트
    counter[fruits[end]] += 1

    # 종류가 3개가 넘어가면 2개 이하가 될때 까지 왼쪽 포인터를 이동
    while len(counter) > 2:
        counter[fruits[start]] -= 1
        # 과일이 0개 되는 종류는 삭제
        if counter[fruits[start]] == 0:
            del counter[fruits[start]]
        start += 1
    # 최대 길이가 정답
    # 아래 코드는 시간초과 됨. 매번 리스트를 복사해서
    # answer = max(answer, len(fruits[start:end + 1]))
    # 그냥 end - start 해도 같음
    answer = max(answer, end - start + 1)
print(answer)
