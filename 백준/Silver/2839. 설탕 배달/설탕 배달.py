import sys
input = sys.stdin.readline

n = int(input())
tmp = 0

# 3만큼 빼다가 5의 배수만큼 남으면 들기.
# 3,5로 안나눠 떨어지면 -1
while n >= 0:
    if n % 5 == 0:
        tmp += (n // 5)
        print(tmp)
        break
    n -= 3
    tmp += 1
else:
    print(-1)