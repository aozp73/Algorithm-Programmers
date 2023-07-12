'유니온 파인드'
# from collections import Counter

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, x, y):
#     a = find_parent(parent, x)
#     b = find_parent(parent, y)
#     if a > b:
#         parent[b] = a
#     else:
#         parent[a] = b
        
# def solution(n, computers):
#     parent = [0] * n
#     for i in range(n):
#         parent[i] = i
        
#     for i in range(0, n - 1):
#         for j in range(i + 1, n):
#             if computers[i][j] == 1:
#               union_parent(parent, i, j)
            
#     for i in range(n):
#         find_parent(parent, i)

#     counter = Counter(parent)
#     cnt = 0
#     for value in counter.values():
#         if value >= 1:
#             cnt += 1
    
#     return cnt

# print(solution(3, 	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

'DFS'
# def solution(n, computers):
#     answer = 0
#     visited = [0 for _ in range(n)]
#     def dfs(computer):
#         visited[computer] = 1
#         for connect in range(n):
#             if visited[connect] == 0 and computers[computer][connect] == 1:
#                 dfs(connect)

#     for computer in range(n):
#         if visited[computer] == 0:
#             dfs(computer)
#             answer += 1
            
#     return answer

'BFS'
# from collections import deque

# def solution(n, computers):
#     answer = 0
#     visited = [0 for _ in range(n)]
#     def bfs(computer):
#         queue = deque([computer])
#         while queue:
#             computer = queue.popleft()
#             visited[computer] = 1
#             for connect in range(n):
#                 if visited[connect] == 0 and computers[computer][connect] == 1:
#                     queue.append(connect)

#     for computer in range(n):
#         if visited[computer] == 0:
#             bfs(computer)
#             answer += 1
            
#     return answer

