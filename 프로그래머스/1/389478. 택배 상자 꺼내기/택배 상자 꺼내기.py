def solution(n, w, num):
    
    num_line = num % (2*w)      # 타켓과 순방향 라인 맨 아래 상자
    inv_line = ((2*w+1) - (num%(2*w))) %(2*w)   # 타겟과 역방향 라인의 맨 아래 상자 
                                                # 2w+1을 0으로 생각하고 역순으로 num을 센다고 생각하면 편하다. 
                                                # 그러면 num과 같은 열을 찾을 수 있다. 
            
    distance = (inv_line - num_line)%(2*w)  # num와 바로 윗 상자와의 거리
    
    ans1 = len(range(num, n+1, 2*w)) 
    ans2 = len(range(num + distance , n+1, 2*w))  
    # 2라인씩 
    return ans1+ans2
