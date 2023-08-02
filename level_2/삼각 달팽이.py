def solution(n):
    triangle = [[0] * i for i in range(1, n+1)] # 삼각형 모양의 2차원 배열 생성
    x, y, num = -1, 0, 1 # 초기 좌표 및 시작 숫자 설정, (0,0)에서 시작하도록 세팅
    
    for i in range(n):        # n 번 반복
        for j in range(i, n): # 내부 반복문
            
            if i % 3 == 0: # 시계 반대 방향으로 채우기 위한 조건
                x += 1     # 다음 리스트로 이동 (좌하단 방향)
            elif i % 3 == 1:
                y += 1     # 해당 리스트에서 우측으로 이동 (우측 방향)
            elif i % 3 == 2:
                x -= 1     # 이전 리스트의 이전 인덱스로 이동 (위쪽 방향)
                y -= 1
                
            triangle[x][y] = num
            num += 1
            
    return [cell for row in triangle for cell in row]

print(solution(4))