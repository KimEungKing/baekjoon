import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    if n == '0':
        break
    # 뒤집어도 같으면 팰린드롬
    if n == n[::-1] :
        print('yes')
    else :
        print('no')
