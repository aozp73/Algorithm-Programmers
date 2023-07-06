# from itertools import product

# def solution(word):
#     answer = []
#     word_list = ['A', 'E', 'I', 'O', 'U']
    
#     for i in range(1,6):
#         for reapet_case in product(word_list,repeat = i):
#             answer.append(''.join(reapet_case))
#     answer.sort()
    
#     return answer.index(word)+1