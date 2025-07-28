import sys
input = sys.stdin.readline

arr = [list(map(int,input().split())) for _ in range(3)]
x1 = y1 = 1001
x2 = y2 = 0

for x,y in arr:
    # x1, x2
    # y1, y2
    if x < x1 :
        x1 = x
    if x > x2:
        x2 = x

    if y < y1:
        y1 = y
    if y > y2:
        y2 = y

answer = [[x1,y1],[x2,y1],[x1,y2],[x2,y2]]
for x,y in answer:
    if [x,y] in arr:
        continue
    else:
        print(x,y)
