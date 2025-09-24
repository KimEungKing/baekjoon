def solution(n):
    # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,... 
    arr = [0] * (n+1)
    arr[1] = 1 
    for i in range(2,n+1):
        arr[i] = arr[i-1] + arr[i-2]
    
    return arr[n]%1234567