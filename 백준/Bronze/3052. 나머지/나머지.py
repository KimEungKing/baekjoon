import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(10)]
result = [arr[i]%42 for i in range(10)]

print(len(set(result)))