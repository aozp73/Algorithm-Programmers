def solution(s):
    wt = 0
    for k in s:
        if k == '(':
            wt += 1
        else: 
            wt -= 1
        if wt < 0: return False
    return wt == 0
    

print(solution("(()("))