def solution(park, routes):
    h = len(park)
    w = len(park[0])
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x,y = j,i

    dx,dy = [1,0,-1,0],[0,1,0,-1] # e, s, w, n
    dir_ = {'E':0,'S':1,'W':2,'N':3}
    
    for i in routes:
        d, n = i.split()
        tmp = dir_[d]
        canmove = True
        nx,ny = x,y 
        
        for _ in range(int(n)):
            nx += dx[tmp]
            ny += dy[tmp]
            if not (0<= nx <w and 0<= ny <h):
                canmove = False
                break
            
            if park[ny][nx] == 'X':
                canmove = False
                break   
                
        if canmove:
            x,y = nx, ny
            
    return [y,x]