import sys
input = sys.stdin.readline

n,m = map(int,input().split())
dict = {}
for i in range(1,n+1):
    dict[i] = input().rstrip()
# value 로 key를 찾는건 시간이 오래걸림 O(n)
# value와 key 값이 반대로 구성된 dict하나 더 만들어주는게 효율적
reverse_dict = {v:k for k,v in dict.items()}

for _ in range(m):
    tmp = input().rstrip()
    if tmp[0].isdigit():
        print(dict[int(tmp)])
    else:
        print(reverse_dict[tmp])
