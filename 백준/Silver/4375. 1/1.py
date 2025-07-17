import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input())
    except:
        break

    i = 1
    s = '1'
    while True:
        if int(s) % n == 0 :
            break
        else:
            s+='1'
            i += 1
    print(i)