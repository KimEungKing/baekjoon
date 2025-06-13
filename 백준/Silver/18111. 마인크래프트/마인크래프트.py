import sys

input = sys.stdin.readline

# 브루트포스
n, m, b = map(int, input().split())
# 2차원으로 받지 말고 1차원 리스트로 받아서 효율 높이기
arr = []
for _ in range(n):
    arr += list(map(int, input().split()))
min_time = [10**9, 0]
for h in range(257):
    use = 0
    get = 0
    for i in range(len(arr)):
        if h < arr[i]:
            get += arr[i] - h
        else:
            use += h - arr[i]

    if use > get + b:
        continue

    if min_time[0] >= get * 2 + use:
        min_time[0] = get * 2 + use
        min_time[1] = h
print(*min_time)
