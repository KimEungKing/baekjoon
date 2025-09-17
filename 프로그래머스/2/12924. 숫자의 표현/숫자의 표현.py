def solution(n):
    answer = 0
    current_sum = 0
    start = 1 
    
    for end in range(1, n + 1):
        current_sum += end 
        
        while current_sum > n:
            current_sum -= start
            start += 1
        
        if current_sum == n:
            answer += 1
            
    return answer