'1. 사전 자료형'
# def solution(clothes):
#     clothes_hash = {}
#     for clothe, type in clothes:
#         clothes_hash[type] = clothes_hash.get(type, 0) + 1
        
#     answer = 1
#     for type in clothes_hash:
#         answer *= (clothes_hash[type] + 1)

#     return answer - 1

'2. Counter'
# from collections import Counter

# def solution(clothes):
#     counter = Counter([type for clothe, type in clothes])

#     answer = 1
#     for count in counter.values():
#         answer *= (count + 1)

#     return answer - 1