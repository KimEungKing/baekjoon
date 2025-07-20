import sys
input = sys.stdin.readline

def push_front(q, n):
    q.insert(0,n)
def push_back(q, n):
    q.append(n)
def pop_front(q):
    if q:
        print(q.pop(0))
    else:
        print(-1)
def pop_back(q):
    if q:
        print(q.pop())
    else:
        print(-1)
def size(q):
    print(len(q))
def empty(q):
    if q:
        print(0)
    else:
        print(1)
def front(q):
    if not q:
        print(-1)
    else:
        print(q[0])
def back(q):
    if not q:
        print(-1)
    else:
        print(q[-1])

n = int(input())
q = []
for _ in range(n):
    tmp = list(input().rstrip().split())
    f = tmp[0]
    if f == 'push_back' or f == 'push_front':
        a = int(tmp[1])
        globals()[f](q,a)
    else:
        globals()[f](q)