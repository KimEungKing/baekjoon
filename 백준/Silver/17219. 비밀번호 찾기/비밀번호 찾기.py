import sys
input = sys.stdin.readline

# n,m 최대 10만
n,m = map(int,input().split())
memo = {}
for _ in range(n):
    site, password = input().rstrip().split(' ')
    memo[site] = password

for _ in range(m):
    tmp = input().rstrip()
    print(memo[tmp])
