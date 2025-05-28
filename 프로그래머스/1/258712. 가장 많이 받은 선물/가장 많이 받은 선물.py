def solution(friends, gifts):
    answer = 0
    giftscore=[0 for _ in range(len(friends))]  #선물지수
    dp = [[0]*len(friends) for _ in range(len(friends))]    
    nxtmon = [0 for _ in range(len(friends))]   #다음달 받을 선물 
    
    for i in range(len(gifts)):
        give,take = gifts[i].split()
        
        #열: 준사람 / 행: 받은사람 
        dp[friends.index(give)][friends.index(take)] += 1
        
        #선물지수 계산
        giftscore[friends.index(give)] += 1
        giftscore[friends.index(take)] -= 1 
    
    # 다음달 받을 선물 계산
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            # 서로에게 받은 것 보다 준 게 많으면 
            if dp[i][j] < dp[j][i]:
                nxtmon[j] +=1
            # 주고받은게 같으면
            elif dp[i][j] == dp[j][i] and i!=j:
                #선물지수 높은 사람한테 다음달 선물 
                if giftscore[i] > giftscore[j]:
                    nxtmon[i]+=1
                elif giftscore[i] > giftscore[j]:
                    nxtmon[j]+=1
    
    answer=max(nxtmon)
    return answer
