import sys
input = sys.stdin.readline

n, m = map(int,input().split())
r,c,d = map(int, input().split())
room = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
dr = [-1,0,1,0]
dc = [0,1,0,-1]

while 1:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.

    if room[r][c] == 0 :
        cnt += 1
        room[r][c] = 2
    if 0 < r < n-1 and 0 < c < m-1:
        # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
        #    주변 4칸이 벽이거나 청소됐거나.
        if room[r-1][c] in (1,2) and room[r+1][c] in (1,2) and room[r][c-1] in (1,2) and room[r][c+1] in (1,2) :
            # 2-1 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            if room[r-dr[d]][c-dc[d]] != 1:
                r = r-dr[d]
                c = c-dc[d]
                continue
            # 2-2 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            else:
                break
        # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
        else:
            # 3-1. 반시계 방향으로 90도 회전한다.
            d = (d+3)%4
            # 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
            if room[r+dr[d]][c+dc[d]] == 0:
                r = r+dr[d]
                c = c+dc[d]

    else:
        break

print(cnt)