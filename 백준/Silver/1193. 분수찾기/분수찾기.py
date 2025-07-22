import sys
input = sys.stdin.readline

# [0,0]
# [0,1] [1,0]
# [2,0] [1,1] [0,2]
# [0,3] [1,2] [2,1] [3,0]

# 1/1
# 1/2 2/1
# 3/1 2/2 1/3
# 1/4 2/3 3/2 4/1       짝수 줄 증가/감소
# 5/1 4/2 3/3 2/4 1/5   홀수 줄 감소/증가

n = int(input())
line = 1 # 몇번째 줄인지 체크
answer = ''
while n/line > 1:
    n -= line
    line += 1

if line % 2:
    answer = str(line + 1 - n) + '/' + str(n)
else:
    answer = str(n) + '/' + str(line+1-n)
print(answer)
