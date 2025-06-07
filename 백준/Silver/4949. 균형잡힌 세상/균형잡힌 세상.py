import sys
input = sys.stdin.readline

while True:
    n = input().rstrip()
    if n == '.':
        break
        
    s = []
    v = True # 괄호 짝이 맞는지 확인용 
    
    for i in n:
        if i in ('(', '['):
            s.append(i)
    
        elif i == ')':
            if not s or s[-1] != '(':
                v = False
                break
            s.pop()
        elif i == ']':
            if not s or s[-1] != '[':
                v = False
                break
            s.pop()
    
    if not s and v:
        print('yes')
    else:
        print('no')