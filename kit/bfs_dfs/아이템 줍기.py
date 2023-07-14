from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    field = [[-1] * 102 for i in range(102)]

    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
            	# x1, x2, y1, y2 테두리 제외, 내부만 0으로 채움
                # 직사각형이 포개질 때, 겹쳐지는 부분은 0으로 채워 짐 
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                    
                # 테두리 이면서, 다른 직사각형의 내부가 아니면 1로 채움 
                elif field[i][j] != 0:
                    field[i][j] = 1
    
    # 동 남 북 서
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # 캐릭터 출발지점 세팅
    q = deque()
    q.append([characterX * 2, characterY * 2])
    visited = [[1] * 102 for i in range(102)]
    
    while q:
        x, y = q.popleft()
        # 도착 지점이 아이템 위치라면, 아이템 까지의 최단거리 / 2를 저장하고 while문 탈출
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            # 이동 좌표가 테두리이면서 아직 방문하지 않은 곳이라면 q에 추가 + visited에 최단거리 갱신
            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    
    return answer