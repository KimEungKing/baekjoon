import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
# print(a**b%c) # 초과
# print(pow(a,b,c))

# 제곱 곱
arr = bin(b)
arr = list(arr[2:])
arr.reverse()
answer = 1
current = a % c

for n in arr:
    if n == '1':
        answer = answer * current % c
    current = current * current % c
print(answer)
