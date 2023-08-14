from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start, end, maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    queue = deque([start])
    visited[start[0]][start[1]] = True
    distance = [[0] * len(maps[0]) for _ in range(len(maps))]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                continue
            
            if not visited[nx][ny] and maps[nx][ny] != "X":
                queue.append((nx, ny))
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1

    return distance[end[0]][end[1]] if visited[end[0]][end[1]] else -1


def solution(maps):
    n, m = len(maps), len(maps[0])
    start, lever, end = (0, 0), (0, 0), (0, 0)
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)
            elif maps[i][j] == "E":
                end = (i, j)

    to_lever = bfs(start, lever, maps)
    if to_lever == -1:
        return -1
    
    to_exit = bfs(lever, end, maps)
    if to_exit == -1:
        return -1
    return to_lever + to_exit

