import sys
input = sys.stdin.readline

# N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 수) 와 같다.
# ..., 9666, 10666,...100666,106660, 106661
N = int(input())
i,cnt = 666,0

while True:
    if '666' in str(i):
        cnt += 1
    if cnt == N:
        print(i)
        break
    i += 1


