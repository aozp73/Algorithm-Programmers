'BFS'
# def solution(numbers, target):
#     cal_res = [0]
#     for number in numbers:
        
#         temp = []
#         for num in cal_res:
#              temp.append(num + number)
#              temp.append(num - number)
        
#         cal_res = temp
    
#     cnt = 0
#     for num in cal_res:
#         if num == target:
#             cnt += 1
    
#     return cnt

# print(solution([1, 1, 1, 1, 1], 3))

'DFS'
# def dfs(idx, cal, number_list, target):
#     global cnt
    
#     if idx == len(number_list):
#         if cal == target:
#             cnt += 1
#             return
#     else:
#         dfs(idx + 1, cal + number_list[idx], number_list, target)
#         dfs(idx + 1, cal - number_list[idx], number_list, target)
        

# def solution(numbers, target):
#     global cnt
#     cnt = 0
#     dfs(0, 0, numbers, target)
    
#     return cnt

# print(solution([1, 1, 1, 1, 1], 3))