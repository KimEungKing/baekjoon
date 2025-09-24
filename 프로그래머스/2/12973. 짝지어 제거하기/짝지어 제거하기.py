def solution(s):
    stk = [] 
    
    for i in s:
        if not stk or stk[-1] != i:
            stk.append(i)
        else:
            stk.pop()
        
        
    if not stk:
        return 1
    else:
        return 0 