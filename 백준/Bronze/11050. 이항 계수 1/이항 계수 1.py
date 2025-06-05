import sys
input = sys.stdin.readline
import math

# N 개중에서 K개를 고르는 수
# nCk
# n! / (k!(n-k)!)
# def factorial(n):
#     if n == 1 :
#         return 1
#     return n * factorial(n-1)

n,k = map(int,input().split())
print(math.factorial(n)//(math.factorial(k)*math.factorial(n-k)))