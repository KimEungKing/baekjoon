import sys
input = sys.stdin.readline

# 키, 몸무게 모두 더 높아야 덩치가 더 크다.
# 둘 중 하나만 크고 하나는 작으면 같은 등수
# 브루트포스

n = int(input())
people = [tuple(map(int, input().split())) for _ in range(n)]
ranks = []

for i in range(n):
    rank = 1  # 처음엔 1등으로 시작
    for j in range(n):
        if i == j:
            continue
        # i 번째 사람보다 큰 사람 몇명 있는지 체크
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1
    ranks.append(rank)

print(*ranks)