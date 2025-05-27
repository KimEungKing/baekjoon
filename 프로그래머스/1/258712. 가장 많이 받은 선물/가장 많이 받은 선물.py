def solution(friends, gifts):
    answer = 0
    giftscore=[0 for _ in range(len(friends))]
    dp = [[0]*len(friends) for _ in range(len(friends))]
    nxtmon = [0 for _ in range(len(friends))]
    
    for i in range(len(gifts)):
        give,take = gifts[i].split()
        dp[friends.index(give)][friends.index(take)] += 1
        giftscore[friends.index(give)] += 1
        giftscore[friends.index(take)] -= 1
    
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            if dp[i][j] < dp[j][i]:
                nxtmon[j] +=1
            elif dp[i][j] == dp[j][i] and i!=j:
                if giftscore[i] > giftscore[j]:
                    nxtmon[i]+=1
                elif giftscore[i] > giftscore[j]:
                    nxtmon[j]+=1
    answer=max(nxtmon)
    return answer