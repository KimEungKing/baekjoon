def solution(left, right):
    # arr = [i for i in range(left,right+1)]
    answer = 0 
    for i in range(left,right+1): 
        if int(i**0.5) == i**0.5: # odd
            answer -= i
        else:
            answer += i
    return answer
            
        
        
    #### 약수를 구할 필요가 없음. 약수가 짝수인지 홀수인지만 판별하면 됨 
#         # 약수 개수 구하기 
#         for n in range(1,int(i**0.5) + 1):
#             if i % n == 0:
#                 if not n*n == i:
#                     cnt += 2
#                 else:
#                     cnt += 1
                    
#         if cnt % 2 == 0 :
#             answer += i
#         else:
#             answer -= i
            
                    