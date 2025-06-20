import sys
input = sys.stdin.readline

n = int(input())    # 최대 100만
m = int(input())    # 최대 100만
s = input().rstrip()
answer = 0

# p = 'I'
# p += 'OI' * n

# for i in range(m):       # 시간 초과
#     if s[i:i+len(p)] == p :
#         answer += 1


# 연속된 oi의 갯수가 몇개인지 카운트
# 만약 n보다 크다면 ex) n==3, 연속된 oi == 4, oi - (n-1)
cnt = 0
isOpen = False # I로 시작 했는지
i = 0
while i < m-2:
    if s[i] == 'I':
        isOpen = True
        i += 1
        while isOpen:
            # print('isopen')
            if s[i:i+2] == 'OI':
                cnt += 1
                i += 2
                # print('if oi')
            else:
                # print('else')
                isOpen = False
    else:
        i+=1
    # print(i)
    if cnt >= n:
        answer += cnt -(n-1)
    cnt = 0
print(answer)