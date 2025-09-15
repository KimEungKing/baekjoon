def solution(x, n):
    if x: 
        return list(range(x,x*(n+1),x))
    else:
        return [0] * n