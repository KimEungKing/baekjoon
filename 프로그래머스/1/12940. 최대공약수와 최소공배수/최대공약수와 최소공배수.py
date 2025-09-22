def solution(n, m):
    answer = []
    a = max(n,m)
    b = min(n,m)
    #gcd
    while b != 0 :
        tmp = b
        b = a%b
        a = tmp
    answer.append(tmp)
    #lcm
    answer.append(n*m//answer[0])
    
    return answer