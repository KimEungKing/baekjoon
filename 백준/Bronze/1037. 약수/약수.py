import sys
input = sys.stdin.readline

# 공배수 ?
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
print(arr[0]*arr[-1])
