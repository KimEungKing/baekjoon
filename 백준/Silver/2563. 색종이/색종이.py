import sys
input = sys.stdin.readline

n = int(input())
paper = [[0]*100 for _ in range(100)]
for _ in range(n):
    x, y = map(int,input().split())
    x -= 1
    y -= 1

    for i in range(10):
        if y+i > 99:
            break

        for j in range(10):
            if x+j > 99:
                break
            paper[y+i][x+j] = 1

answer = 0
for i in range(100):
    answer += sum(paper[i])

print(answer)