import sys
input = sys.stdin.readline

n = int(input())
n_lst = set(map(int,input().split()))
m = int(input())
m_lst = list(map(int,input().split()))

for i in m_lst:
    if i in n_lst:
        print(1)
    else:
        print(0)