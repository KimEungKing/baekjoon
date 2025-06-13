import sys

input = sys.stdin.readline


def split_paper(x, y, n):
    color = paper[y][x]
    # 색이 같은지 확인 
    for i in range(y, y + n):
        for j in range(x, x + n):
            if paper[i][j] != color:
                # 다른게 있으면 4등분 
                split_paper(x, y, n // 2)
                split_paper(x + n // 2, y, n // 2)
                split_paper(x, y + n // 2, n // 2)
                split_paper(x + n // 2, y + n // 2, n // 2)
                return
            
    # 종이 색이 다 같다면
    global white, blue
    if color:
        blue += 1
    else:
        white += 1


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
blue = 0
white = 0
split_paper(0, 0, n)
print(white)
print(blue)
