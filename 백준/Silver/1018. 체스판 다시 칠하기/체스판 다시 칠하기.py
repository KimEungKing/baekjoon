import sys
input = sys.stdin.readline

n,m = map(int,input().split())
minimum = 64
arr = [input().rstrip() for _ in range(n)]
cmp1 = 'BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB'
cmp2 = 'WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW'
for i in range(n-7):
    for j in range(m-7):
        extract = ''
        for k in range(8):  # 8*8 만큼씩 추출해서 
            extract += arr[i+k][j:j+8]
        # 바꿔야하는 개수를 세서 가장 작은걸 minimum에 
        minimum = min(minimum,sum(c1 != c2 for c1,c2 in zip(cmp1,extract)),sum(c1 != c2 for c1,c2 in zip(cmp2,extract)))

print(minimum)