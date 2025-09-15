def solution(s):
    if len(s) in [4,6]:
        return s.isdigit()
    else:
        return False