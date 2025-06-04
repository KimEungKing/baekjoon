import sys
input = sys.stdin.readline

num = list(map(int,input().split()))
num.sort()

# 유클리드 호제법
# 2개의 자연수 a, b(a > b)에 대해서 a를 b로 나눈 나머지가 r일 때, a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# 큰 수를 작은 수로 계속 나눠서 0이 되는 작은 수가 최대공약수
b = num[0]
a = num[1]
while b != 0:
    r = a%b # 큰수를 작은 수로 나눈 나머지.
    a = b   # 큰수랑 작은 수 위치 바꿔주기
    b = r
print(a)

# 최소 공배수 : a*b 를 a,b의 최대공약수로 나눈 것 과 같다.
print(num[0] * num[1]//a)