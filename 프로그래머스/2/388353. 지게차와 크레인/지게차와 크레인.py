def checkoutside(arr, a, b, visited):
    if visited[a][b]:
        return False
    visited[a][b] = True

    if a == 0 or b == 0 or a == len(arr)-1 or b == len(arr[0])-1:
        return True  # 바깥쪽과 연결됨
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        na = a + dx[i]
        nb = b + dy[i]
        if 0<=na<len(arr) and 0<=nb<len(arr[0]):
            if arr[na][nb] == '0':
                if checkoutside(arr,na,nb,visited):
                    return True
    return False 
    

def crane(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == target:
                arr[i][j] = '0'
    return arr

def forklift(arr, target):
    tmp = [] 
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == target:
                visited = [[False]*len(arr[0]) for _ in range(len(arr))]
                if checkoutside(arr,i,j,visited):
                    tmp.append([i,j])
    
    for i,j in tmp:
        arr[i][j] = '0'
         
    return arr

def solution(storage, requests):
    n,m = len(storage),len(storage[0])
    arr = [['0'] * (m+2) for _ in range(n+2)] #패딩
    for i in range(1,n+1):
        for j in range(1,m+1):
            arr[i][j] = storage[i-1][j-1]

    for i in requests:
        if len(i) == 1 :
            arr = forklift(arr,i[0])
        else:
            arr = crane(arr,i[0])
            
    print(arr)
    
    cnt = 0
    for i in arr:
        cnt += len(i) - i.count('0')

    return cnt