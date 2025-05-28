def solution(data, ext, val_ext, sort_by):
    answer = []
    # 숫자로 변경 
    key_dict = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    ext_n = key_dict[ext]
    sort_by_n = key_dict[sort_by]
    
    for i in range(len(data)):
        if data[i][ext_n] < val_ext:
            answer.append(data[i])
    
    answer.sort(key = lambda x : x[sort_by_n])
    
    return answer