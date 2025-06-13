def solution(name, yearning, photo):
    answer = []
    y_d = {n:i for n,i in zip(name,yearning)}
    
    for i in photo:
        sum_y = 0
        for j in i:
            if j in y_d: 
                sum_y += y_d[j]
        answer.append(sum_y)
        
    return answer