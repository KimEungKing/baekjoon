def solution(schedules, timelogs, startday):
    # schedules : 출근 희망 시간
    # timelog : [i][요일별 실제 출근 시간]
    allowed = []    # 출근 허용시간 
    answer = 0
    cnt = [0 for _ in range(len(schedules))] # 카운트용 
    
    for i in range(len(schedules)):
        allowed.append(schedules[i]+10)
        if allowed[i]%100 >= 60:
            allowed[i] += 40 # +100-60
    
    for i in range(len(timelogs)):
        t = startday
        for j in range(7):
            if (timelogs[i][j] <= allowed[i]) and (t!=6 and t!=7) :
                cnt[i] += 1
                print(t)
            if t >7 :    # 8 -> 1 로 초기화 해주지 않으면 startday 가 7일 때 문제 생김 
                t = 1 
            t += 1
            
    answer = cnt.count(5)

    return answer
