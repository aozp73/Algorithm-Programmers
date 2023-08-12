def solution(data, col, row_begin, row_end):
    # 첫 번째 정렬 조건: col 번째 컬럼의 오름차순 정렬
    # 두 번째 정렬 조건: 첫 번째 컬럼의 내림차순 정렬
    data.sort(key=lambda x: (x[col-1], -x[0]))

    # 해시 값 계산
    result = 0
    for i in range(row_begin, row_end+1):
        S_i = sum([data[i-1][j] % i for j in range(len(data[0]))])
        result ^= S_i

    return result