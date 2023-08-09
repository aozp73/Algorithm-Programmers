def is_valid(x, y): # 대기실 내의 좌표인지 확인
    return 0 <= x < 5 and 0 <= y < 5

def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P': # 응시자 위치에서 진행
                # 맨해튼 거리가 1인 위치
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = i + dx, j + dy
                    if is_valid(nx, ny) and place[nx][ny] == 'P':
                        return False
                
                # 맨해튼 거리가 2인 위치
                for dx, dy in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
                    nx, ny = i + dx, j + dy
                    if is_valid(nx, ny) and place[nx][ny] == 'P':
                        # 파티션 확인
                        if dx == 2:
                            if place[i+1][j] != 'X':
                                return False
                        elif dx == -2:
                            if place[i-1][j] != 'X':
                                return False
                        elif dy == 2:
                            if place[i][j+1] != 'X':
                                return False
                        elif dy == -2:
                            if place[i][j-1] != 'X':
                                return False
                
                # 대각선 위치
                for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                    nx, ny = i + dx, j + dy
                    if is_valid(nx, ny) and place[nx][ny] == 'P':
                        # 대각선에 파티션이 있는지 확인
                        if place[i][ny] != 'X' or place[nx][j] != 'X': 
                            return False

    return True

def solution(places):
    return [1 if check(place) else 0 for place in places]