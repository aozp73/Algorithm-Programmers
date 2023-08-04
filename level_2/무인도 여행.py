'DFS'
# import sys
# sys.setrecursionlimit(10**6)

# # 동 남 북 서 (시계 방향)
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def dfs(x, y, maps, visited):
#     visited[x][y] = True
#     days = int(maps[x][y])
    
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
    
#         # 맵을 벗어나지 않고, 바다가 아니며, 방문하지 않았을 때 진행
#         if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]) or visited[nx][ny] or maps[nx][ny] == 'X':
#             continue
#         days += dfs(nx, ny, maps, visited)
        
#     return days

# def solution(maps):
#     visited = [[False] * len(maps[0]) for _ in range(len(maps))]
#     result = []
    
#     for i in range(len(maps)):
#         for j in range(len(maps[0])):
#             if maps[i][j] != 'X' and not visited[i][j]:
#                 result.append(dfs(i, j, maps, visited))
                
#     return sorted(result) if result else [-1]

'BFS'
# from collections import deque

# # 동 남 북 서 (시계 방향)
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def bfs(x, y, maps, visited):
    
#     queue = deque([(x, y)])
#     visited[x][y] = True
#     days = int(maps[x][y])
    
#     while queue:
#         x, y = queue.popleft()
        
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             # 맵을 벗어나지 않고, 바다가 아니며, 방문하지 않았을 때 진행
#             if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]) or visited[nx][ny] or maps[nx][ny] == 'X':
#                 continue
            
#             visited[nx][ny] = True
#             days += int(maps[nx][ny])
#             queue.append((nx, ny))
            
#     return days

# def solution(maps):
#     visited = [[False] * len(maps[0]) for _ in range(len(maps))]
#     result = []
    
#     for i in range(len(maps)):
#         for j in range(len(maps[0])):
#             if maps[i][j] != 'X' and not visited[i][j]:
#                 result.append(bfs(i, j, maps, visited))
                
#     return sorted(result) if result else [-1]
