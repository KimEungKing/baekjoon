import sys

input = sys.stdin.readline

# n 100만 , m 20억 , 나무 최대 높이 10억
n, m = map(int, input().split())
trees = list(map(int, input().split()))
# 브루트포스 당연히 시간초과, 이분탐색으로 풀어야함
start = 0
end = max(trees)

while start <= end:
    h = (start + end) // 2
    total = 0

    for tree in trees:
        if tree > h:
            total += tree - h

    if total >= m:
        start = h + 1
    else:
        end = h - 1

# start 는 h를 높이는데 이용,
# end 는 가장 높은 h였던 것
print(end)

