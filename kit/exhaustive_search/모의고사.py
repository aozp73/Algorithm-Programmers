'진행 코드'
# import heapq

# def solution(answers):
    
#     stu_1 = [1, 2, 3, 4, 5]
#     stu_2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     stu_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#     cnt = [0, 0, 0]
    
#     for index, answer in enumerate(answers):
        
#         if stu_1[index % 5] == answer:
#             cnt[0] += 1
#         if stu_2[index % 8] == answer:
#             cnt[1] += 1
#         if stu_3[index % 10] == answer:
#             cnt[2] += 1
    
#     heap = [(-cnt[0], 1), (-cnt[1], 2), (-cnt[2], 3)]
#     heapq.heapify(heap)
#     max_stu = heapq.heappop(heap)
    
    
#     answer = []
#     if max_stu[1] == 0:
#         return []
#     else:
#         answer.append(max_stu[1])
#     for _ in range(2):
#         stu = heapq.heappop(heap)
#         if  stu[0] == max_stu[0]:
#             answer.append(stu[1])
        
#     return answer

# print(solution([1,3,2,4,2]))

'리펙토링'
# import heapq

# def solution(answers):
    
#     stu_1 = [1, 2, 3, 4, 5]
#     stu_2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     stu_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#     cnt = [0, 0, 0]
#     res = []
    
#     for index, answer in enumerate(answers):
        
#         if stu_1[index % 5] == answer:
#             cnt[0] += 1
#         if stu_2[index % 8] == answer:
#             cnt[1] += 1
#         if stu_3[index % 10] == answer:
#             cnt[2] += 1
    
#     for idx, s in enumerate(cnt):
#         if s == max(cnt):
#             res.append(idx + 1)
        
#     return res