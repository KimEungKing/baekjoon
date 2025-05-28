def solution(s):
    stack = []
    
    for i in s :
        if i == '(':
            stack.append(1)
        else :
            if len(stack)==0:
                return False
            stack.pop()
    if stack :
        return False
    else: 
        return True 