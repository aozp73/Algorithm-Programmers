def solution(board):
    # 행과 열의 길이
    row_len = len(board)
    col_len = len(board[0])

    max_side = 0 # 최대 변의 길이를 저장할 변수

    # 행이나 열의 길이가 1인 경우, 최대 정사각형의 한 변의 길이는 1
    if row_len < 2 or col_len < 2:
        return 1

    # 각 칸을 돌면서 최대 변의 길이를 구함
    for i in range(1, row_len):
        for j in range(1, col_len):
            # 현재 칸의 값이 1인 경우
            if board[i][j] != 0:
                # 주변 3칸 (왼쪽, 왼쪽 위, 위쪽) 중 최솟값에 1을 더한 값을 현재 칸에 저장
                board[i][j] = min(board[i-1][j], board[i-1][j-1], board[i][j-1]) + 1
                # 현재 칸의 값이 최대 변의 길이보다 크다면, 최대 변의 길이를 갱신
                max_side = max(max_side, board[i][j])

    # 최대 변의 길이를 제곱하여 정사각형의 넓이를 반환
    return max_side ** 2