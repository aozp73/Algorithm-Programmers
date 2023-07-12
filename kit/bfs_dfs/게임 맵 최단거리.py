from collections import deque

def bfs(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0] * m for _ in range(n)]  
    res = [[0] * m for _ in range(n)] 
    
    # 동 남 서 북
    dx = [0, 1, 0, -1]  
    dy = [1, 0, -1, 0]
    
    queue = deque([(0, 0)]) 
    visited[0][0] = 1 
    res[0][0] = 1 
    
    while queue:  
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not 0 <= nx < n or not 0 <= ny < m: 
                continue
                
            if visited[nx][ny] == 1 or maps[nx][ny] == 0:  
                continue
                
            visited[nx][ny] = 1  
            res[nx][ny] = res[x][y] + 1  
            queue.append((nx, ny))  

    val = res[n-1][m-1]     
    if val == 0:  
        return -1
    else:
        return val
    

def solution(maps):
    return bfs(maps)


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))