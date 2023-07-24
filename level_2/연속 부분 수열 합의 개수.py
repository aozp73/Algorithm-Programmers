'시간복잡도 높은 풀이'
# def solution(elements):
#     s_new_elements = elements[:]
#     s_new_elements.extend(elements)
#     s_check = set()

#     for i in range(len(elements)):
#         for j in range(i, i + len(elements)): 
#             s_check.add(sum(s_new_elements[i : j+1]))

#     return len(s_check)

# print(solution([7, 9, 1, 1, 4]))


'시간복잡도 개선'
# def solution(elements):
#     s_new_elements = elements[:]
#     s_new_elements.extend(elements)
#     s_check = set()
#     length = len(elements)
    
#     for i in range(len(elements)):
#         sum = 0
#         for j in range(i, i + length):
#             sum += s_new_elements[j]
#             s_check.add(sum)

#     return len(s_check)

# print(solution([7, 9, 1, 1, 4]))