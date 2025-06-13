def solution(players, callings):
    # list.index() -> 시간 초과
    # 딕셔너리 사용 (인덱스 == 순위 )
    d = {p:i for i,p in enumerate(players)}
    
    for call in callings:
        idx = d[call]
        players[idx],players[idx-1] = players[idx-1],players[idx]
        
        # 순위(인덱스) 변경 
        # 이미 순서는 바뀌었으니 딕셔너리 업데이트
        d[players[idx]] = idx
        d[players[idx-1]] = idx-1 
        
    return players