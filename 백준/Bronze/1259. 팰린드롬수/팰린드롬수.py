import sys
input = sys.stdin.readline

# 절반으로 나눠서 앞/뒤 스트링 리버스 시켜서 비교
while True:
    n = input().rstrip()
    if n == '0':
        break

    if n == n[::-1] :
        print('yes')
    else :
        print('no')