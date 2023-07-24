def s_rotate(lst):
    return lst[1:] + lst[0]

def s_check(lst):
    s_stack = []
    pairs = {')':'(', ']':'[', '}':'{'}
    
    for char in lst:
        if char in pairs.values():
            s_stack.append(char)
        elif s_stack and s_stack[-1] == pairs[char]:
            s_stack.pop()
        else:
            return False
    
    return len(s_stack) == 0

def solution(s):
    s_cnt = 0
    if s_check(s):
        s_cnt += 1

    for _ in range(len(s) - 1):
        s = s_rotate(s)
        if s_check(s):
            s_cnt += 1

    return s_cnt

print(solution("[](){}"))