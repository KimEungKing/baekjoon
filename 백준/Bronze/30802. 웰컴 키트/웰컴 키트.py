import sys
input = sys.stdin.readline

N = int(input())
t_arr = list(map(int,input().split()))
t,p = map(int,input().split())

# 티셔츠
tcnt = 0
for i in t_arr:
    tcnt += (i+t-1)//t
print(tcnt)
# 펜
print(N//p, N%p)
