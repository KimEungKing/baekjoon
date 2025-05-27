# 함수를 이용하자

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    # 각 시간들을 초로 변경 
    m ,s = map(int,video_len.split(':'))
    total_sec = m*60 + s 
    m ,s = map(int,pos.split(':'))
    pos_sec = m*60 +s 
    m ,s = map(int,op_start.split(':'))
    start_sec = m*60 +s
    m ,s = map(int,op_end.split(':'))
    end_sec = m*60 +s
      
    # 현재 위치가 오프닝 내에 있으면 오프닝 끝으로  
    if pos_sec<= end_sec and pos_sec>=start_sec:
            pos_sec = end_sec       
    
    for i in commands:
        if i == "next":
            pos_sec += 10
            if pos_sec > total_sec:
                pos_sec = total_sec
        elif i =="prev":
            pos_sec -= 10
            if pos_sec < 0 :
                pos_sec = 0
                
        # 커맨드 입력시마다 오프닝에 포함될 시 오프닝 끝으로.        
        if pos_sec<= end_sec and pos_sec>=start_sec:
            pos_sec = end_sec   
            
    res_m = pos_sec//60
    res_s = pos_sec%60
    
    answer = f"{res_m:02d}:{res_s:02d}"
    
    return answer
