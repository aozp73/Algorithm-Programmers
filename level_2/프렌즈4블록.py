def solution(m, n, board):
    answer = 0

    # 2차원 배열로 변환
    board = [list(x) for x in board]

    while True:
        remove_list = [[0] * n for _ in range(m)]

        # 2x2 블록 찾기
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '_':
                    remove_list[i][j] = remove_list[i][j+1] = remove_list[i+1][j] = remove_list[i+1][j+1] = 1

        # 블록 지우기
        for i in range(m):
            for j in range(n):
                if remove_list[i][j] == 1:
                    board[i][j] = '_'
                    answer += 1

        # 블록 내리기
        for _ in range(m):
            for i in range(m-1, 0, -1):
                for j in range(n):
                    if board[i][j] == '_':
                        board[i][j], board[i-1][j] = board[i-1][j], '_'
        
        # 지울 블록이 없다면 종료
        if sum(sum(remove_list, [])) == 0:
            return answer