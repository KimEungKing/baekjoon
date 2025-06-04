import sys
input = sys.stdin.readline

a,b,v = map(int,input().split())

# a-b씩 매일 올라가다가
# 마지막날은 무조건 a 만큼 올라간다.
# 그러면 a-b 씩 카운트 하면 v에서 (a-b)계속 해야하는데 마지막은 a만 들어가니까 +b
# v - (n(a-b)+b) == 0
# v-b - (n(a-b)) == 0
# (v-b) / (a-b) == n

if (v-b)%(a-b) == 0 :
    print((v-b)//(a-b))
else :
    print((v-b+a-b-1)//(a-b)) # 올림

