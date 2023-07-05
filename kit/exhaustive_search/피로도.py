'완전 탐색'
# from itertools import permutations

# def solution(k, dungeons):
#     permu_dungeons = permutations(dungeons, len(dungeons))

#     res = int(-1e9)
#     for dungeons in permu_dungeons:
        
#         user_k = k
#         cnt = 0
#         for n, r in dungeons:
#             if n > user_k:
#                 continue
            
#             if user_k >= r:
#                 cnt += 1
#                 user_k -= r
        
#         res = max(res, cnt)

#     return res

# print(solution(80, [[80,20],[50,40],[30,10]]))

'DFS, 백트래킹'
# answer = 0
# N = 0
# visited = []

# def dfs(k, cnt, dungeons):
#     global answer
#     if cnt > answer:
#         answer = cnt

#     for j in range(N):
#         if k >= dungeons[j][0] and not visited[j]:
#             visited[j] = 1
#             dfs(k - dungeons[j][1], cnt + 1, dungeons)
#             visited[j] = 0


# def solution(k, dungeons):
#     global N, visited
    
#     N = len(dungeons)
#     visited = [0] * N
#     dfs(k, 0, dungeons)
#     return answer