import sys
input = sys.stdin.readline

arr = list(map(int,list(input().rstrip())))
arr.sort(reverse=True)
for i in arr:
    print(i,end='')