def solution(s):
    answer = ''
    s = s.lower()
    arr = list(s)
    is_start = True
    for i in range(len(arr)):
        if is_start and arr[i] != ' ':
            arr[i] = arr[i].upper()
            is_start = False
        elif arr[i] == ' ':
            is_start = True
            
    answer = ''.join(arr)
    return answer