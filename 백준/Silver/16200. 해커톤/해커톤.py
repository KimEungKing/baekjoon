# 각 인원이 속할 수 있는 팀의 최대 크기
# 그리디. 정렬 후 xi 만큼 묶기

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
arr.sort()
cnt = 0
teamsize = 0
nowmax = arr[0]

for i in range(len(arr)):
    teamsize += 1
    if teamsize == nowmax:
        cnt += 1
        teamsize = 0
        if i+1 < N:
            nowmax = arr[i+1]

if teamsize != 0 :
    cnt += 1

print(cnt)
