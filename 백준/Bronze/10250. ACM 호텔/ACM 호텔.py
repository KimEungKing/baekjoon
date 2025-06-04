import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h,w,n = map(int,input().strip().split())
    y = n % h
    if y == 0 :
        y = h
        x = n // h
    else:
        x = (n // h)+1
    print(f'{y:d}{x:02d}')