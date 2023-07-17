'슬라이싱'
def solution(s):
    divide_s = s.split(' ')
    print(divide_s)
    for i in range(len(divide_s)):
        if divide_s[i]:
            if divide_s[i][0].isalpha():
                divide_s[i] = divide_s[i][0].upper() + divide_s[i][1:].lower()
            else:
                divide_s[i] = divide_s[i][0] + divide_s[i][1:].lower() 
            
    return " ".join(divide_s)

print(solution("hello   world"))


'capitalize() 활용'
def solution(s):
    divide_s = s.split(' ')
    
    for i in range(len(divide_s)):
        divide_s[i] = divide_s[i].capitalize()
        
    return " ".join(divide_s)

print(solution("hello   world"))