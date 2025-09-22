def solution(s):
    answer = []
    arr = list(s)
    zerocnt = 0
    cnt = 0
    
    while len(arr) > 1:
        zerocnt += arr.count('0')
        cnt += 1 
        arr = list(bin(len(arr) - arr.count('0'))[2:])
        
    answer = [cnt, zerocnt]
    return answer