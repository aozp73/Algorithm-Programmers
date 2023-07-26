def solution(msg):
    # 사전 초기화
    dictionary = {chr(65 + i): i + 1 for i in range(26)}
    dict_index = 27

    i = 0
    answer = []
    while i < len(msg):
        # 최대한 긴 단어 찾기
        j = 1
        while i + j <= len(msg) and msg[i:i+j] in dictionary:
            j += 1
        # 현재 단어의 색인 번호를 결과에 추가
        answer.append(dictionary[msg[i:i+j-1]])
        
        # 새로운 단어를 사전에 추가
        dictionary[msg[i:i+j]] = dict_index
        
        dict_index += 1
        i = i + j - 1

    return answer

print(solution("KAKAO"))