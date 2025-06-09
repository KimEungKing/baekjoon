import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
arr = [int(input()) for _ in range(n)]
def myround(x):
    if x < 0:
        return int(x-0.5)
    else:
        return int(x+0.5)
# 산술평균
print(myround(sum(arr)/n))

# 중앙값
print(sorted(arr)[int(n//2)])

# 최빈값
counter = Counter(arr)
mode = counter.most_common()
mode.sort(key= lambda x:(-x[1],x[0]))   # 빈도수 많은거 먼저, 작은 값 먼저.
mode = mode[:2]
if len(mode)==1:
    print(mode[0][0])
else:
    if mode[0][1] > mode[1][1]:
        print(mode[0][0])
    else:
        print(mode[1][0])

# 최댓값 - 최솟값
print(max(arr)-min(arr))