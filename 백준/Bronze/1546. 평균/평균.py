n = int(input())
score = list(map(int,input().split()))
score2 = [x/max(score)*100 for x in score]
print(sum(score2)/len(score2))