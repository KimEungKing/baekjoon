  # park의 빈 공간중 가장 큰 square 찾기 
  # dp
def find_empty_square(arr):

    matrix = arr[:]
    row = len(matrix)
    col = len(matrix[0])
    dp = [[0]*col for _ in range(row)]
    max_side = 0
    
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == '-1':
                if i==0 or j==0 :
                    dp[i][j] = 1 
                else :
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
            max_side = max(max_side,dp[i][j])
    
    return max_side 

def solution(mats, park):
    answer=-1
    max_side = find_empty_square(park)
    
    for i in range(len(mats)):
        if mats[i] > max_side or answer > mats[i]:
            continue
        else:
            answer = mats[i] 
    return answer