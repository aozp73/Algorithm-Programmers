'1. 집합자료형'
# def solution(nums):
#     answer = 0
    
#     n = len(nums)
#     num_nums = set(nums)
#     if len(num_nums) < n // 2:
#         answer = len(num_nums)
#     else:
#         answer = n // 2

#     return answer

# def solution(nums):
#     return min(len(nums)/2, len(set(nums)))

'2. Counter'
# from collections import Counter

# def solution(nums):
#     return min(len(Counter(nums)), len(nums) // 2)