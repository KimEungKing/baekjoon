import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

# 에라토스테네스의 체
e = [0,0] # 수는 1000 이하 자연수
for i in range(2,1001):
    e.append(i) # 인덱스와 값이 일치하게 2 ~ 1000

for i in range(2,1001):
    if e[i] == 0:
        continue
    for j in range(i*i,1001,i):
        e[j] = 0

set(e)
cnt = 0
for i in arr:
    if i in e:
        cnt +=1
print(cnt)