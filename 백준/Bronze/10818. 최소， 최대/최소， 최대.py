import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

print(min(arr),max(arr))