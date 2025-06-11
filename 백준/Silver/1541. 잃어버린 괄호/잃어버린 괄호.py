import sys
input = sys.stdin.readline

# - 기준으로 나눠서 
s = input().rstrip()
parts = list(s.split('-'))

# 나눠진 파트끼리 계산하고 
arr = []
for i in parts:
    tmp = sum(map(int,i.split('+')))
    arr.append(tmp)
answer = arr[0]

# 첫번째 파트 - 나머지파트 
for i in range(1,len(arr)):
    answer -= arr[i]
print(answer)