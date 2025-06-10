def solution(triangle):
    dp = [i[:] for i in triangle]

    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            # 줄의 첫 칸
            if j == 0 :
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            #줄의 마지막칸
            elif j == i : 
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            
            else:
                # 윗 줄의 두개 중 큰 값과 더해넣음 
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
    
    return max(dp[-1])