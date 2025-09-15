def solution(arr):
    answer = []
    m = min(arr)
    if len(arr) == 1 :
        answer = [-1]
    else:
        for i in arr:
            if not i == m:
                answer.append(i)
    return answer