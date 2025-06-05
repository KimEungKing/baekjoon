import sys
input = sys.stdin.readline

# 1, 2, fizz, 4 ,buzz ...

s = [input().rstrip() for _ in range(3)]
num = 0
for i in range(3):
    if s[i].isdigit():
        num = int(s[i]) + 2-i + 1# 가장 마지막입력을 숫자로 바꾼 값의 다음 값

if num%15 == 0 :    #3,5 가 먼저 오면 먼저 걸러져서
    print('FizzBuzz')
elif num%3 == 0:
    print('Fizz')
elif num%5 == 0:
    print('Buzz')
else:
    print(num)

