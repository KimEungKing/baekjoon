import sys
input = sys.stdin.readline

arr = list(map(int,input().split()))
sqrarr = [i*i for i in arr]

print(sum(sqrarr)%10)