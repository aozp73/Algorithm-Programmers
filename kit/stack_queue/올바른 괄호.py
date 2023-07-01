'풀이 1) 단순 변수 활용'

# def solution(s):
#     if s[0] == ')':
#         return False
    
#     left_cnt = 0
#     right_cnt = 0
#     check = 0
    
#     answer = True
    
#     for k in s:
#         if k == '(':
#             left_cnt +=1
#             check += 1
#         else:
#             right_cnt +=1
#             check -= 1
        
#         if check < 0:
#             return False
        
#     if left_cnt != right_cnt:
#         answer = False
    
#     return answer
'최적화'
# def solution(s):
#     wt = 0
#     for c in s :
#         if c == '(' : wt += 1
#         elif c == ')' : wt -= 1
#         if wt < 0 : return False
#     return wt == 0


'풀이 2 스택 활용'
# def solution(s):
#     stack = []
#     for i in s:
#         # 스택이 비어있는데 닫힌괄호 들어오는 경우: False 
#         if len(stack) == 0 and i == ')':
#             return False

#         # 스택 맨 위 열린괄호 -> 닫힌괄호 들어오는 경우: pop
#         if stack[-1] == '(' and i == ')':
#             stack.pop()

#         # 열린 괄호 들어오는 경우: append
#         if i == '(':
#             stack.append('(')

#     # 다 끝났는데 남아있으면: False 
#     return False if len(stack) != 0 else True
