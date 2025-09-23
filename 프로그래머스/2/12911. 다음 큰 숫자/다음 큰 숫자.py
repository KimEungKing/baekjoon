def solution(n):
    answer = n
    while 1:
        answer += 1 
        if bin(n)[2:].count('1') == bin(answer)[2:].count('1') : 
            break
        
    return answer