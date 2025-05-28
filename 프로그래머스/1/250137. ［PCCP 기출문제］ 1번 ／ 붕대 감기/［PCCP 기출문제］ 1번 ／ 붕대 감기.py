def solution(bandage, health, attacks):
    answer = 0
    band_t = 0  #밴디지 감는 시간 
    attack_cnt = 0 #공격 횟수 카운트
    max_health = health #최대체력
    
    #공격 시간 만큼
    for i in range(1,attacks[-1][0]+1):
        # 회복 계산 (공격 안당할 때)
        if attacks[attack_cnt][0] != i :
            band_t +=1
            health += bandage[1]

            # 붕대 풀로 감았을 때
            if band_t >= bandage[0] :
                health += bandage[2]
                band_t=0
            # 최대체력 
            if health > max_health : 
                health = max_health 
            print(i,health,band_t)

        # 공격 계산
        else :
            health -= attacks[attack_cnt][1]
            band_t = 0
            attack_cnt += 1 
            print(i,'attack',health,band_t)
                
        #죽는경우
        if health <= 0:
            answer=-1
            break

        answer = health
        
    return answer