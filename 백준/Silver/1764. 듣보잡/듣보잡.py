import sys
input = sys.stdin.readline

# n,m 최대 50만
n,m = map(int,input().split())
n_set = {input().rstrip() for _ in range(n)}
m_set = {input().rstrip() for _ in range(m)}
answer = []

for i in n_set:
    if i in m_set:
        answer.append(i)
answer.sort()
# answer = sorted(n_set & m_set) 

print(len(answer))
for i in answer:
    print(i)