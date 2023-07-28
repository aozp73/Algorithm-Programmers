def solution(land):
    s_row = len(land)
    s_column = len(land[0]) # 4고정
    
    s_index_check = -1
    s_sum = 0
    
    for i in range(s_row):
        max = -1
        for idx, num in enumerate(land[i]):
            if idx == s_index_check:
                continue
            if num > max:
                max = num
                s_index_check = idx
        print(max)
        print(s_index_check)
        s_sum += max

    return s_sum

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))