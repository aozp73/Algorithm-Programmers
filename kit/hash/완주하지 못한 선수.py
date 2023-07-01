'1. 단순 반복'
# def solution(participant, completion):
    
#     answer = ''
#     participant.sort()
#     completion.sort()
    
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             answer = participant[i]
#             break
            
#     if answer == '':
#         answer = participant[len(participant) - 1]

#     return answer

'2. 사전자료형 + 해시값'
# def solution(participant, completion):
#     participant_dict = {} # 빈 사전자료형 생성
#     sumHash = 0
    
#     for part in participant:
#         participant_dict[hash(part)] = part
#         sumHash += hash(part)
        
#     for comp in completion:
#         sumHash -= hash(comp)
        
#     answer = participant_dict[sumHash]
        
#     return answer

'3. Counter'
# import collections
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
    
#     return list(answer.keys())[0]
