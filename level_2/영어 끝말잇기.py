'하나씩 구현'
# def solution(n, words):

#     s_cnt_round = 1 # 몇 번째 판인지 체크
#     s_cnt = 1 # 몇 번째 사람인지 체크
#     s_prev_word = words[0]
#     s_check = [words[0]]
#     s_flag = True
    
#     for i in range(1, len(words)):
#         if s_cnt == n:
#             s_cnt = 1
#             s_cnt_round += 1
#         else:
#             s_cnt += 1
        
#         word = words[i]
        
#         if word in s_check:
#             s_flag = False
#             break
        
#         s_check.append(word)
#         if s_prev_word[-1] != word[0]:
#             s_flag = False
#             break
        
#         s_prev_word = word

#     if s_cnt_round == len(words) / n and s_cnt == n and s_flag == True:
#         s_cnt_round, s_cnt = 0, 0

#     return [s_cnt, s_cnt_round]

# print(solution(2, 	["hello", "one", "even", "never", "now", "world", "draw"]))

'간결화'
# def solution(n, words):
#     for i in range(1, len(words)):
#         # 이전 단어의 마지막 문자와 현재 단어의 첫 문자가 일치하지 않거나,
#         # 이미 사용된 단어라면 바로 [참가자 번호, 참가 순서] 반환
#         if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
#             return [i % n + 1, i // n + 1]
    
#     # 조건을 모두 만족했다면 [0, 0] 반환
#     return [0, 0]

# print(solution(2, 	["hello", "one", "even", "never", "now", "world", "draw"]))