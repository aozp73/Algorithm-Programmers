def solution(n, t, m, p):

    # 구해야할 진수 1의 자리 갯수 = 차례(1바퀴) + 명수(2바퀴) + 명수(3바퀴) (미리 구할 숫자 바퀴까지)
    s_cnt = p
    for _ in range(t-1):
        s_cnt += m
    hex_map = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        
    # 1의 자리로 분리하여 해당 진수에 맞게 값 넣기 (구해야할 갯수 만큼 반복)    
    s_num = 0
    converted = "0"
    while len(converted) <= s_cnt:
        s_num += 1
        temp_num = s_num
        converted_num = ""
        while temp_num > 0:
            temp_num, mod = divmod(temp_num, n)
            # 10~15의 경우 대문자 A~F로 변환
            if mod >= 10:
                mod = hex_map[mod]
            converted_num = str(mod) + converted_num
        converted = converted + converted_num
   
    # 뽑아야 할 인덱스 순회하여 출력
    s_tube_turn = p - 1
    answer = converted[s_tube_turn]
    for _ in range(t - 1):
        s_tube_turn += m
        answer += converted[s_tube_turn]
        
    return answer