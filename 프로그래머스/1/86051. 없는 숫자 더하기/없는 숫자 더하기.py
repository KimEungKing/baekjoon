def solution(numbers):
    answer = 1+2+3+4+5+6+7+8+9
    for i in numbers:
        answer -= i
    return answer